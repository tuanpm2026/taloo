# Taloo — hướng dẫn cho agent

Đây là core sinh truyện dùng chung. Bộ nhân vật Cảnh sát trưởng Labrado đã được nghiên cứu riêng theo yêu cầu người dùng tại `Characters/CHARACTERS.md`; đọc hồ sơ và xem refs liên quan trước khi viết truyện/prompt cho bộ này. Không tự lấy dữ liệu hoặc quy tắc riêng của series nguồn.

- Đọc `CLAUDE.md` để nắm quy trình.
- Với bộ Labrado, đọc thêm `Characters/SUPPORTING_CHARACTERS.md` và `Characters/CHARACTER_SHEETS.md`. Dùng sheet trong `Characters/sheets/` làm ref nhất quán cho tranh; đối chiếu refs gốc khi cần xác nhận thiết kế trong phim. Chi tiết khuất do AI bổ sung không phải dữ kiện nguồn.
- Phân biệt thỏ Pipi và thỏ mặc váy đỏ; hai em Papillon giữ ID theo màu, không đoán tên Pudding/Puff.
- Mỗi truyện ở `story-N/`: `content` → `image-prompts-plan.md` → `cover.png`, `pageK.png` → `narration.json`, `audio/` → `index.html`.
- Khi lập prompt ảnh, theo `.claude/skills/story-prompts/SKILL.md`; khi tạo slideshow/giọng đọc, theo `.claude/skills/story-slideshow/SKILL.md`.
- Nhân vật và phong cách lấy từ yêu cầu hiện tại và tài liệu của dự án, nếu có. Không tự điền đặc điểm chưa biết mà ảnh/truyện cần dùng.
- Sửa template/công cụ nguồn rồi build HTML bằng `tools/build_story_slideshow.py` và `tools/build_webapp.py`.
- Chạy `tools/validate_series.py` trước khi xuất bản có truyện.
- Ảnh thật, ảnh tham chiếu và ảnh gốc lưu local. `docs/` là bản có thể đưa lên web; duyệt nội dung với người dùng trước khi đăng công khai, trừ khi đã được cho phép trong phiên làm việc.

- Bé Shopee là nhân vật riêng do người dùng cung cấp, 3 tuổi. Đọc `Characters/SHOPEE.md`, dùng `Characters/sheets/shopee.png` trước khi sinh tranh có bé.
