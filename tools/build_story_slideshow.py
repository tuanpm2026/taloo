#!/usr/bin/env python3
"""Build index.html slideshow cho truyện từ narration.json + template.

Usage:
    python3 tools/build_story_slideshow.py story-1

Đọc <story-dir>/narration.json, fill vào tools/slideshow_template.html,
ghi ra <story-dir>/index.html, rồi kiểm tra mọi asset (ảnh + mp3) tồn tại.
"""
import json
import sys
from pathlib import Path
from reader_i18n import localize_reader

PLACEHOLDERS = ("__TITLE__", "__START_SUB__", "__COVER__", "__SLIDES_JSON__")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: build_story_slideshow.py <story-dir>")

    story_dir = Path(sys.argv[1]).resolve()
    plan_path = story_dir / "narration.json"
    if not plan_path.exists():
        sys.exit(f"Không tìm thấy {plan_path}")

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    slides = plan["slides"]
    language = plan.get("language", "vi")
    count = len(slides) - 1
    subtitle = (f"Read and listen &nbsp;•&nbsp; {count} pages" if language.startswith("en")
                else f"Nghe kể chuyện &nbsp;•&nbsp; {count} trang")

    template = (Path(__file__).parent / "slideshow_template.html").read_text(encoding="utf-8")
    html = (
        template
        .replace("__TITLE__", plan["title"])
        .replace("__START_SUB__", subtitle)
        .replace("__COVER__", slides[0]["image"])
        .replace("__SLIDES_JSON__", json.dumps(slides, ensure_ascii=False, indent=2))
    )
    html = localize_reader(html, language)

    leftover = [p for p in PLACEHOLDERS if p in html]
    if leftover:
        sys.exit(f"Template còn placeholder chưa fill: {leftover}")

    out_path = story_dir / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"✓ {out_path} ({len(slides)} slides)")

    missing = []
    for slide in slides:
        for key in ("image", "audio"):
            asset = story_dir / slide[key]
            if not asset.is_file() or asset.stat().st_size == 0:
                missing.append(slide[key])
    if missing:
        print("⚠ Asset thiếu hoặc rỗng:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    print(f"✓ Đủ {len(slides) * 2} asset (ảnh + audio)")


if __name__ == "__main__":
    main()
