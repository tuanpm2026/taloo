# Character sheet cho Taloo

Tạo ngày 02/10/2026 bằng **ImageGen tích hợp**, từ ảnh tham chiếu đã lưu. Có **12 sheet 3D**, mỗi sheet gồm toàn thân chính diện, góc ba phần tư và nghiêng. Xem [gallery](sheets/index.html) hoặc mở từng PNG bên dưới.

Đây là **ảnh AI tạo cho dự án**, không phải model sheet chính thức của BabyBus. Ảnh nguồn được giữ nguyên trong `refs/`; nguồn và checksum nằm trong [SOURCES.json](SOURCES.json). Hồ sơ nhân vật xem [CHARACTERS.md](CHARACTERS.md) và [SUPPORTING_CHARACTERS.md](SUPPORTING_CHARACTERS.md).

| ID | Nhân vật | Sheet AI | Tham chiếu |
|---|---|---|---|
| labrador | Cảnh sát trưởng Labrado | [Sheet](sheets/labrador.png) | [Ref gốc](refs/labrador.png) |
| doberman | Cảnh sát Dober | [Sheet](sheets/doberman.png) | [Ref gốc](refs/doberman.png) |
| papillon | Cảnh sát Papillon | [Sheet](sheets/papillon.png) | [Ref gốc](refs/papillon.png) |
| antel | Tiến sĩ Antel | [Sheet](sheets/antel.png) | [Ref gốc](refs/antel.png) |
| dodo | Dodo | [Sheet](sheets/dodo.png) | [Ref gốc](refs/dodo-clear.jpg) |
| little-rabbit | Thỏ con (váy đỏ) | [Sheet](sheets/little-rabbit.png) | [Ref gốc](refs/little-rabbit.jpg) |
| little-duck | Vịt con | [Sheet](sheets/little-duck.png) | [Ref gốc](refs/little-duck.jpg) |
| little-rhino | Tê giác con | [Sheet](sheets/little-rhino.png) | [Ref gốc](refs/little-rhino.jpg) |
| pipi-rabbit | Thỏ Pipi | [Sheet](sheets/pipi-rabbit.png) | [Ref gốc](refs/pipi-rabbit-3d.jpg) |
| little-chick | Gà con | [Sheet](sheets/little-chick.png) | [Ref gốc](refs/little-chick.jpg) |
| papillon-sibling-orange | Em Papillon — màu cam | [Sheet](sheets/papillon-sibling-orange.png) | [Ref gốc](refs/pudding-puff.jpg) |
| papillon-sibling-pink | Em Papillon — màu hồng | [Sheet](sheets/papillon-sibling-pink.png) | [Ref gốc](refs/pudding-puff.jpg) |

## Cách sử dụng

- Dùng sheet tương ứng làm ref nhận diện khi sinh tranh, kèm mô tả nhân vật và yêu cầu hành động của cảnh. Chỉ đưa các nhân vật thực sự xuất hiện.
- Phần chân, giày, lưng và trang phục bị khuất trong ảnh nguồn được AI hoàn thiện; không dùng phần bổ sung này làm bằng chứng về thiết kế trong phim. Đặc biệt chân của Antel/Dodo và trang phục dưới của Gà con cần coi là lựa chọn của bộ sheet Taloo.
- Refs nhân vật phụ là thumbnail quảng bá 3D từ kênh chính thức; một số tập dùng hoạt hình 2D. Sheet thống nhất theo thiết kế 3D trong thumbnail đã chọn.
- Thỏ Pipi đội mũ/tai nghe và Thỏ con mặc váy đỏ là hai thiết kế riêng. Không gộp chúng.
- Cặp em của Papillon thuộc nhóm Pudding–Puff, nhưng chưa xác minh tên ứng với màu nào. Giữ ID theo màu cam/hồng; không tự gán tên hoặc giới tính.
- Các sheet riêng không xác nhận tỷ lệ chiều cao giữa nhân vật. Khi vẽ chung cần chọn tỷ lệ nhất quán cho cảnh.

## Prompt và kiểm tra

[CHARACTER_SHEET_PROMPTS.json](CHARACTER_SHEET_PROMPTS.json) lưu đầy đủ 12 prompt, ref đầu vào, đường dẫn đầu ra, trạng thái, công cụ và SHA-256. Đã xem từng ảnh để kiểm tra ba góc toàn thân, nhận diện/trang phục chính, nền sạch và không lẫn nhân vật khác. Mặt sau chưa có view riêng; góc nghiêng không thay thế một sheet quay đủ vòng.

## Bé Shopee — bổ sung

Bổ sung [sheet bé Shopee 3 tuổi](sheets/shopee.png) và [ảnh riêng](portraits/shopee.png) từ ảnh mẫu người dùng; tổng gallery hiện có 13 nhân vật. Hồ sơ tại [SHOPEE.md](SHOPEE.md), prompt riêng tại [SHOPEE_PROMPTS.json](SHOPEE_PROMPTS.json).
