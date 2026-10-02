---
name: story-slideshow
description: Build HTML slideshow with Vietnamese TTS voice for a story in the Taloo series. Auto-trigger when the user asks to make slideshow/slide/voice/audio/giọng đọc/đọc truyện/thuyết minh for a `story-N/` folder, or wants an index.html that reads the story aloud over the page images. Reads `content` + `image-prompts-plan.md`, writes `narration.json`, gens `audio/*.mp3` via edge-tts (voice HoaiMy), builds self-contained `index.html` from template. Skill is project-local for the Taloo series only.
---

# Story → HTML Slideshow + Voice

Tạo slideshow HTML tự chứa (ảnh + giọng đọc tiếng Việt) cho một truyện trong series **Taloo**. Mở bằng browser từ `file://`, không cần server/mạng sau khi gen.

## Pipeline (3 bước + verify)

```
content + image-prompts-plan.md
        │  (bước 1 — bước duy nhất cần suy nghĩ)
        ▼
narration.json ──(bước 2: tools/gen_story_audio.py)──► audio/*.mp3
        │
        └──(bước 3: tools/build_story_slideshow.py)──► index.html
```

## Bước 0 — Kiểm tra đầu vào

```bash
ls story-N/          # cần: content, cover.png, page1..K.png, image-prompts-plan.md
```

- **Đếm số `pageK.png` thực tế** — số trang ảnh có thể ít hơn số scene trong plan (plan là đề xuất, ảnh là sự thật). Slides = `cover.png` + `page1..K.png` theo đúng số file thật.
- Nếu thiếu `narration.json` mới làm bước 1; nếu đã có thì tái sử dụng, chỉ sửa khi yêu cầu hiện tại cần thay đổi lời đọc.
- edge-tts nằm ở venv: `.venv/bin/python` (cài theo README.md và requirements.txt).

## Bước 1 — Viết `narration.json` (cạnh file `content`)

Schema:

```json
{
  "title": "Tên truyện lấy từ dòng 'Bài học:' trong content",
  "voice": "vi-VN-HoaiMyNeural",
  "rate": "-10%",
  "slides": [
    { "image": "cover.png", "audio": "audio/00-cover.mp3", "text": "..." },
    { "image": "page1.png", "audio": "audio/01.mp3", "text": "..." }
  ]
}
```

### Quy tắc chia & viết lời đọc (HARD RULES)

1. **Mapping trang ↔ đoạn truyện:** dùng heading `SCENE K` trong `image-prompts-plan.md` để biết trang `pageK.png` vẽ cảnh gì, rồi cắt đoạn `content` tương ứng. Cover = tựa truyện + câu "Bài học hôm nay: …" (từ dòng `Chủ đề:`). Trang cuối (infographic) = mục "Bài học cho bé" cuối content.
2. **Trung thành với lời truyện** — không sáng tác thêm tình tiết. Chỉ được biến đổi cho hợp giọng kể.
3. **Lời thoại dạng kịch bản phải chuyển thành văn kể:** `Nhân vật: "..."` → `Nhân vật dặn: "..."` / `Nhân vật đáp:` — chọn động từ theo ngữ cảnh. TTS đọc liền mạch, không đọc tên nhân vật khô khan.
4. **Danh sách bài học đọc bằng chữ số đếm tiếng Việt:** "Một, … Hai, … Ba, …" (không dùng "1." — TTS có thể đọc thành "một chấm").
5. **Mỗi slide một đoạn text trọn vẹn** — người nghe hiểu được khi chỉ nghe trang đó. Trang quá dài (>~60s đọc) thì cân nhắc cắt bớt mô tả phụ, giữ thoại chính.
6. **Voice mặc định `vi-VN-HoaiMyNeural`, rate `-10%`** (mặc định đọc chậm cho bé, có thể đổi trong narration.json). Giọng nam thay thế: `vi-VN-NamMinhNeural`.
   Với truyện tiếng Anh, đặt `language: "en-US"`, chọn giọng tiếng Anh đang có trên dịch vụ (ví dụ `en-US-JennyNeural`) và giữ toàn bộ lời đọc bằng tiếng Anh. Tool build dùng `language` để chuyển giao diện đọc sang tiếng Anh; không tự thêm câu dẫn hay bài học tiếng Việt. Có thể đặt `end_pause_ms` trên slide kết bằng câu hỏi để chừa thời gian cho bé trả lời (0–10000 ms).
7. Tên riêng tiếng nước ngoài: để nguyên lần đầu; nếu user phàn nàn cách phát âm thì phiên âm trong `text` (vd "Rai-đơ") — lưu ý text này cũng là caption hiển thị, nên chỉ phiên âm khi user yêu cầu.

## Bước 2 — Gen audio

```bash
.venv/bin/python tools/gen_story_audio.py story-N
```

- Script tự retry khi Edge TTS lỗi `NoAudioReceived` (lỗi ngẫu nhiên thường gặp) và sleep 1.5s giữa các request để tránh throttle.
- File 0 byte = chưa gen (script tự coi như missing và gen lại; `--force` để gen lại tất cả).
- **Verify bắt buộc** sau khi gen:

```bash
for f in story-N/audio/*.mp3; do ffprobe -v error -show_entries format=duration -of csv=p=0 "$f" || echo "HỎNG: $f"; done
```

Mọi file phải ra duration > 0. File hỏng → xoá rồi chạy lại script.

## Bước 3 — Build index.html

```bash
python3 tools/build_story_slideshow.py story-N
```

- **KHÔNG viết tay index.html** — template duy nhất ở `tools/slideshow_template.html` (sửa giao diện thì sửa template rồi rebuild các truyện).
- Script tự fill `__TITLE__ / __VOICE_LABEL__ / __SLIDE_COUNT__ / __COVER__ / __SLIDES_JSON__` và **tự verify mọi asset tồn tại & khác rỗng** (exit 1 nếu thiếu).
- Lý do nhúng SLIDES thẳng vào HTML: `fetch()` JSON bị CORS chặn trên `file://`.

## Bước 4 — Nghiệm thu

```bash
open story-N/index.html
```

Nhắc user kiểm tra: (1) bấm "Bắt đầu đọc truyện" → audio chạy + tự lật trang khi đọc xong; (2) giọng đọc tên riêng có ổn không; (3) nút Aa ẩn/hiện caption; (4) tap mép trái/phải lật trang.

## Template features (đã có sẵn, đừng làm lại)

Start overlay (bắt buộc vì autoplay policy của browser), auto-advance sau audio +1s, tap zones trái/phải, dots điều hướng, nút ⏮ ▶/⏸ ⏭ 🔁 Aa, caption bật sẵn, end overlay "Đọc lại từ đầu", phím tắt ←/→/Space, preload ảnh trang kế.

## Checklist hoàn thành

- [ ] Đếm đúng số page ảnh thực tế
- [ ] `narration.json` đủ cover + mọi trang, thoại đã chuyển văn kể
- [ ] `audio/*.mp3` đủ, ffprobe pass hết
- [ ] `build_story_slideshow.py` chạy pass (đủ asset)
- [ ] Mở browser cho user nghiệm thu
