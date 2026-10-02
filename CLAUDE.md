# Taloo

Quy trình tạo truyện tranh tiếng Việt. Core không gắn cứng nhân vật; dự án hiện có hồ sơ riêng của bộ Cảnh sát trưởng Labrado.

## Đầu vào

- Yêu cầu về chủ đề, độ tuổi độc giả, nhân vật và phong cách.
- `story-N/content`: tiêu đề `Bài học:`, chủ đề `Chủ đề:`, nội dung và mục `Bài học cho bé`.
- Bộ nhân vật hiện tại: `Characters/CHARACTERS.md`, refs chính thức của BabyBus tại `Characters/refs/`; nguồn tại `Characters/SOURCES.json`. Đọc hồ sơ và xem refs trước khi viết prompt.
- Nhân vật phụ: `Characters/SUPPORTING_CHARACTERS.md`. Bộ 12 sheet AI: `Characters/CHARACTER_SHEETS.md`, ảnh tại `Characters/sheets/`; dùng sheet tương ứng để giữ thiết kế nhất quán khi sinh tranh. Không coi chi tiết AI hoàn thiện là xác nhận chính thức.
- Giữ thỏ Pipi tách khỏi thỏ mặc váy đỏ; không gán tên Pudding/Puff cho hai em Papillon khi chưa xác minh.
- Phân biệt hồ sơ chính thức, mô tả quan sát từ ảnh, thông tin wiki bổ sung và đề xuất sáng tác. Không tự điền chi tiết còn chưa xác minh.

## Quy trình

1. Viết nội dung theo yêu cầu, nhất quán với mô tả nhân vật đã được xác định.
2. Skill `story-prompts` → `story-N/image-prompts-plan.md`.
3. Tạo ảnh → `cover.png`, `page1.png` … `pageK.png`.
4. Skill `story-slideshow` → `narration.json`, `audio/*.mp3`, `index.html`.
5. Validate → build thư viện → xuất `docs/` khi cần.

## Mặc định kỹ thuật

- Khung dọc 5:7; giữ safe margin cho in A5.
- Gen ảnh thử với chất lượng thấp và ref nhỏ để tiết kiệm; nâng chất lượng khi cần in.
- Giọng đọc Edge TTS `vi-VN-HoaiMyNeural`, rate `-10%`; có thể đổi theo từng `narration.json`.
- Phong cách minh hoạ phải nhất quán trong cả truyện, lấy từ yêu cầu hoặc refs của dự án.
- Lỗi ảnh lặp lại thì cập nhật quy tắc trong skill, không chỉ sửa từng prompt.
- Nội dung và refs gốc lưu local; bản web trong `docs/` cần duyệt trước khi đăng công khai.

Xem `README.md` để cài dependency và chạy công cụ.
