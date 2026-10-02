#!/usr/bin/env python3
"""Gen audio mp3 cho slideshow truyện từ narration.json bằng edge-tts.

Usage:
    .venv/bin/python tools/gen_story_audio.py story-1 [--force] [--continue-on-error]

Đọc <story-dir>/narration.json, gen từng slide ra <story-dir>/audio/*.mp3.
Bỏ qua file đã tồn tại trừ khi có --force. --continue-on-error thử các slide
sau nếu một slide bị dịch vụ từ chối tạm thời, rồi báo các file còn thiếu.
"""
import asyncio
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import edge_tts


async def gen_one(text: str, voice: str, rate: str, out_path: Path, retries: int = 4) -> None:
    for attempt in range(1, retries + 1):
        try:
            communicate = edge_tts.Communicate(text, voice=voice, rate=rate)
            await communicate.save(str(out_path))
            print(f"  ✓ {out_path.name} ({out_path.stat().st_size // 1024} KB)")
            return
        except Exception as exc:  # NoAudioReceived / network — thử lại với backoff
            if out_path.exists():
                out_path.unlink()
            if attempt == retries:
                raise
            wait = 3 * attempt
            print(f"  ! {out_path.name} lỗi ({exc.__class__.__name__}), thử lại sau {wait}s...")
            await asyncio.sleep(wait)


def add_end_pause(out_path: Path, milliseconds: int) -> None:
    """Leave time for a child to answer a page's closing question."""
    if not 0 <= milliseconds <= 10000:
        raise ValueError("end_pause_ms must be between 0 and 10000")
    if milliseconds == 0:
        return
    with tempfile.TemporaryDirectory(prefix="taloo-audio-") as directory:
        padded = Path(directory) / "padded.mp3"
        subprocess.run([
            "ffmpeg", "-v", "error", "-y", "-i", str(out_path),
            "-af", f"apad=pad_dur={milliseconds / 1000}",
            "-codec:a", "libmp3lame", "-b:a", "128k", str(padded),
        ], check=True)
        out_path.write_bytes(padded.read_bytes())


async def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    continue_on_error = "--continue-on-error" in sys.argv
    if not args:
        sys.exit("Usage: gen_story_audio.py <story-dir> [--force]")

    story_dir = Path(args[0]).resolve()
    plan_path = story_dir / "narration.json"
    if not plan_path.exists():
        sys.exit(f"Không tìm thấy {plan_path}")

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    voice = plan.get("voice", "vi-VN-HoaiMyNeural")
    rate = plan.get("rate", "-10%")
    slides = plan["slides"]

    print(f"Story: {plan.get('title', story_dir.name)}")
    print(f"Voice: {voice}  rate: {rate}  slides: {len(slides)}")

    failed = []
    for slide in slides:
        out_path = story_dir / slide["audio"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        if out_path.exists() and out_path.stat().st_size > 0 and not force:
            print(f"  - {out_path.name} đã có, bỏ qua")
            continue
        try:
            await gen_one(slide["text"], voice, rate, out_path)
            add_end_pause(out_path, int(slide.get("end_pause_ms", 0)))
        except Exception as exc:
            if not continue_on_error:
                raise
            failed.append(out_path.name)
            print(f"  ! {out_path.name} bỏ qua sau khi thử lại ({exc.__class__.__name__})")
        await asyncio.sleep(1.5)  # tránh throttle của dịch vụ Edge TTS

    if failed:
        sys.exit("Còn thiếu audio: " + ", ".join(failed))
    print("Xong.")


if __name__ == "__main__":
    asyncio.run(main())
