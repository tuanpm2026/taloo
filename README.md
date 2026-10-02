# Taloo

[Đọc truyện trên GitHub Pages](https://tuanpm2026.github.io/taloo/) · [Nghe truyện mẫu đầy đủ](https://tuanpm2026.github.io/taloo/story-1/audio/full-story.mp3)

Core tạo truyện tranh: nội dung → kế hoạch prompt ảnh → tranh → lời đọc/audio → slideshow → thư viện đọc truyện và bản xuất web. Mặc định tiếng Việt; truyện có thể chọn ngôn ngữ và giọng đọc riêng.

Chuyển từ core Panda-stories, đã bỏ cấu hình nhân vật và nội dung của series nguồn. Truyện thử đầu tiên là **Shopee and the Missing Balloons** tại `story-1/`, bằng tiếng Anh cho bé Shopee 3 tuổi. Bộ nhân vật **Cảnh sát trưởng Labrado** được nghiên cứu và bổ sung riêng theo yêu cầu người dùng tại [Characters/CHARACTERS.md](Characters/CHARACTERS.md), kèm refs gốc lưu local và [nguồn tra cứu](Characters/SOURCES.json). Đã bổ sung [hồ sơ nhân vật phụ](Characters/SUPPORTING_CHARACTERS.md) và [12 character sheet AI](Characters/CHARACTER_SHEETS.md), mỗi sheet có ba góc nhìn. Mở [gallery](Characters/sheets/index.html) để xem và đối chiếu ảnh nguồn.

## Cài đặt

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Dùng Python 3.10 trở lên. Cần `ffprobe` (trong FFmpeg) để kiểm tra audio; cần `cwebp` (trong WebP) để xuất ảnh web. Trên macOS: `brew install ffmpeg webp`.

## Quy trình

1. Tạo `story-N/content`: dòng đầu `Bài học: <tên truyện>`, tiếp theo `Chủ đề: <chủ đề>`, phần truyện và mục cuối `Bài học cho bé`.
2. Theo `.claude/skills/story-prompts/SKILL.md` để viết `story-N/image-prompts-plan.md`. Nhân vật, bối cảnh và phong cách lấy từ yêu cầu riêng của dự án.
3. Tạo ảnh theo plan, lưu `cover.png`, `page1.png` … `pageK.png`. Khung dọc tỷ lệ 5:7.
4. Theo `.claude/skills/story-slideshow/SKILL.md` để viết `story-N/narration.json`, ánh xạ đúng ảnh đã tạo. JSON gồm `title`, `voice`, `rate`, `slides`; mỗi slide có `image`, `audio`, `text`.
   Truyện tiếng Anh đặt thêm `language: "en-US"` và giọng tiếng Anh, ví dụ `voice: "en-US-JennyNeural"`, `rate: "-10%"`. Nội dung đọc và caption đều tiếng Anh; builder chuyển các nút đọc sang tiếng Anh. Slide kết bằng câu hỏi có thể đặt `end_pause_ms: 2500` để chừa thời gian cho bé trả lời.
5. Chạy các công cụ:

```bash
.venv/bin/python tools/gen_story_audio.py story-1
python3 tools/build_story_slideshow.py story-1
python3 tools/validate_series.py
python3 tools/build_webapp.py
```

Mở `story-1/index.html` để đọc một truyện hoặc `index.html` để xem thư viện. HTML nhúng dữ liệu nên có thể mở trực tiếp, không cần server. Audio cần mạng lúc tạo bằng Edge TTS; sau đó có thể nghe offline.

```bash
python3 tools/build_webapp.py --deploy
```

Lệnh này tạo bản xuất trong `docs/`, chuyển ảnh thành WebP và sao chép audio; không sửa ảnh gốc và không tự đăng lên mạng. Có thể dùng `docs/` cho GitHub Pages sau khi duyệt nội dung.

Repository riêng: `tuanpm2026/taloo`. GitHub Pages lấy bản web từ nhánh `main`, thư mục `/docs`. Các thư mục `story-N/` và ảnh nhân vật gốc vẫn ở local theo `.gitignore`; repository lưu công cụ, tài liệu và bản xuất web.

`validate_series.py` tự tìm các thư mục `story-N`, hoặc nhận đường dẫn truyện cụ thể. Kiểm tra đầu vào, tiêu đề, thứ tự trang, tỷ lệ ảnh, lời đọc, đường dẫn asset và thời lượng audio. Khi chưa có truyện, validator báo không tìm thấy và trả exit code 1; trình build thư viện vẫn tạo trang rỗng.

## Công cụ nguồn

- `tools/gen_story_audio.py`: Edge TTS, mặc định HoaiMy `-10%`, retry, bỏ qua audio đã có; hỗ trợ `--force` và `--continue-on-error`.
- `tools/build_story_slideshow.py` + `tools/slideshow_template.html`: slideshow, caption, tự lật trang, bàn phím, điều hướng và giữ màn hình sáng.
- `tools/reader_i18n.py`: nhãn giao diện tiếng Việt/tiếng Anh theo ngôn ngữ truyện; thư viện dùng tiếng Anh khi toàn bộ truyện là tiếng Anh.
- `tools/build_webapp.py`: thư viện nhiều truyện, deep link `#story=N`, tự mở truyện tiếp và bản xuất web.
- `tools/validate_series.py`: kiểm tra bộ truyện trước khi xuất.

Sửa công cụ/template nguồn rồi build lại; không chỉnh HTML sinh ra bằng tay. Nội dung, ảnh gốc và ảnh tham chiếu mặc định chỉ lưu local theo `.gitignore`.
