#!/usr/bin/env python3
"""Validate local story assets before building the reader library."""

import json
import re
import struct
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_ASPECT_RATIO = 5 / 7
# Image generation can vary slightly in canvas size; the reader is screen-first.
SCREEN_ASPECT_TOLERANCE = 0.03


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        header = stream.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    return struct.unpack(">II", header[16:24])


def audio_duration(path: Path) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def validate_story(folder: Path) -> list[str]:
    errors = []
    content = folder / "content"
    narration = folder / "narration.json"
    plan = folder / "image-prompts-plan.md"
    for path in (content, narration, plan):
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing {path.name}")
    if errors:
        return errors

    first_line = content.read_text(encoding="utf-8").splitlines()[0]
    if not first_line.startswith("Bài học: "):
        errors.append("content must begin with 'Bài học: '")
    data = json.loads(narration.read_text(encoding="utf-8"))
    if first_line.startswith("Bài học: ") and data.get("title") != first_line.removeprefix("Bài học: "):
        errors.append("narration title differs from content title")
    slides = data.get("slides", [])
    if len(slides) < 3:
        errors.append("too few slides")
    expected_images = ["cover.png", *(f"page{i}.png" for i in range(1, len(slides)))]
    actual_images = [slide.get("image") for slide in slides]
    if actual_images != expected_images:
        errors.append("image names are not cover.png, page1.png ... in order")
    if len({slide.get("audio") for slide in slides}) != len(slides):
        errors.append("duplicate audio paths")

    for slide in slides:
        if not slide.get("text", "").strip():
            errors.append(f"empty narration for {slide.get('image')}")
        for kind in ("image", "audio"):
            name = slide.get(kind)
            if not isinstance(name, str) or Path(name).is_absolute() or ".." in Path(name).parts:
                errors.append(f"invalid {kind} path: {name}")
                continue
            path = folder / name
            if not path.is_file() or path.stat().st_size == 0:
                errors.append(f"missing or empty {name}")
                continue
            try:
                if kind == "image":
                    width, height = png_size(path)
                    if abs(width / height - TARGET_ASPECT_RATIO) > SCREEN_ASPECT_TOLERANCE:
                        errors.append(f"wrong aspect ratio {name}: {width}x{height}")
                elif audio_duration(path) <= 0:
                    errors.append(f"zero duration {name}")
            except (ValueError, OSError, subprocess.CalledProcessError) as exc:
                errors.append(f"invalid {name}: {exc}")
    return errors


def main() -> int:
    folders = [Path(arg).resolve() for arg in sys.argv[1:]]
    if not folders:
        folders = sorted(
            (p for p in ROOT.glob("story-*") if p.is_dir() and re.fullmatch(r"story-\d+", p.name)),
            key=lambda p: int(re.search(r"(\d+)$", p.name).group(1)),
        )
    if not folders:
        print("No story-N directories found")
        return 1
    failed = False
    for folder in folders:
        errors = validate_story(folder)
        if errors:
            failed = True
            print(f"FAIL {folder.name}: " + "; ".join(errors))
        else:
            print(f"OK   {folder.name}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
