---
name: story-prompts
description: Lập kế hoạch prompt ảnh cho truyện tranh Taloo khi người dùng yêu cầu tạo hoặc sửa prompt/ảnh từ story-N/content. Đọc nội dung và mô tả nhân vật riêng của dự án; viết image-prompts-plan.md gồm cover, các scene, infographic bài học và bảng refs. Hướng dẫn tiếng Việt, prompt tiếng Anh, khung dọc 5:7. Không có nhân vật hay thế giới truyện mặc định.
---

# Story → Image Prompts Plan

Tạo kế hoạch để người dùng hoặc công cụ tạo ảnh thực hiện theo thứ tự. Đây là core quy trình; mọi nhân vật, đặc điểm, bối cảnh và phong cách phải lấy từ yêu cầu hoặc tài liệu dự án.

## Quy tắc bắt buộc

1. **Khoá danh tính nhân vật:** loài, giới tính, tuổi, tỉ lệ, ngoại hình và đại từ đúng mô tả đã xác định. Tên dễ gây hiểu nhầm phải đi kèm mô tả rõ; chỉ dùng negative prompt phù hợp nhân vật hiện tại.
2. **Giải phẫu và đồ vật theo thiết kế:** động vật, người, phương tiện và nhân vật nhân hoá phải bám refs. Không tự áp đặt tay người, mặt trên xe, hoặc cấm chúng nếu thiết kế hiện tại có các đặc điểm đó. Công cụ cơ khí phải mô tả riêng với bộ phận cơ thể.
3. **Chữ có chủ đích:** chặn speech bubbles, dialogue balloons, thought bubbles, random floating text, captions không mong muốn; giữ logo/ký hiệu/trang phục đã được yêu cầu. Không cấm toàn bộ text/words/letters vì có thể mất luôn chữ mong muốn. Cover và infographic phải cho phép chữ tiêu đề.
4. **Trang phục và refs:** tả cụ thể chi tiết nhận dạng và lặp lại mô tả chốt trong từng prompt; chỉ upload refs của nhân vật có mặt trong scene. Giữ logo được yêu cầu nhìn thấy rõ khi bố cục cho phép; chữ nhỏ có thể hậu kỳ.
5. **Chiều sâu:** cảnh rộng/đông cần foreground, midground, background; vật xa nhỏ hơn và hơi mờ, đường dẫn về vanishing point. Dùng upper/lower half khi chia khung dọc.
6. **Dữ liệu đã có:** đọc tài liệu nhân vật nếu có, không hỏi lại thông tin đã xác định. Thiếu ảnh ref thì ghi rõ và thêm prompt character sheet. Chỉ hỏi chi tiết chưa biết cần cho cảnh; không đoán mục TODO/CHỜ XÁC NHẬN.
7. **Tiêu đề:** cover ghi đúng tựa truyện; infographic ghi đúng `Bài học: …`, dấu tiếng Việt, chữ dễ đọc và safe margin. Ghi `render exactly: «…»`; bỏ điều khoản cấm tương ứng nếu scene cần bảng tên hay chữ cụ thể.
8. **Tỉ lệ:** mô tả chiều cao/kích thước tương đối giữa các nhân vật dựa trên dữ liệu hiện tại, tránh tự biến nhân vật thành chibi/toddler hoặc thay đổi tuổi.
9. **Ref nhiều nhân vật:** mô tả đầy đủ màu, trang phục, dáng và dấu hiệu riêng. Nếu ảnh scene đông lệch thiết kế, khoá solo từng nhân vật trước rồi dùng refs đã chọn; sửa cục bộ khi phù hợp.
10. **Vật lý và an toàn:** hành động và tư thế khớp nội dung. Nhân vật trong xe có thân ở trong xe; nếu cảnh cần chớm vi phạm để được nhắc thì mô tả đúng mức đó, không tăng mức nguy hiểm so với truyện.
11. **Địa điểm:** mô tả kiến trúc, đạo cụ, không gian cụ thể thay vì chỉ nêu tên. Bảng tên được yêu cầu phải được cho phép riêng trong prompt.
12. **Cảnh đông:** liệt kê từng nhân vật với một dấu hiệu nhận dạng, tổng số và vị trí; yêu cầu đủ số lượng, không gộp/nhầm. Sau khi tạo ảnh đếm lại và sửa phần thiếu.
13. **Phong cách:** dùng mô tả trực quan của dự án, nhất quán với refs; không dựa vào tên thương hiệu/studio làm mô tả duy nhất. Nếu công cụ không nhận cú pháp `--ar`/`--no`, chuyển thành câu tự nhiên.
14. **Di chuyển/chia tay:** khoá hướng di chuyển so với camera, hướng mặt từng nhân vật và vị trí đối tượng được chào; tránh chỉ viết “looking back” mà không xác định nhìn về đâu.
15. **Ngôn ngữ theo yêu cầu hiện tại:** với truyện tiếng Anh, chữ bìa và infographic đều bằng tiếng Anh; yêu cầu ngôn ngữ của người dùng thay cho các mặc định tiếng Việt bên dưới. Các nhãn metadata nội bộ `Bài học:`/`Chủ đề:` không phải chữ cần đưa vào ảnh hoặc đọc thành tiếng.

## Workflow

1. Xác định `story-N/content`, output cùng thư mục và tài liệu/refs nhân vật nếu dự án đã bổ sung. Đường dẫn người dùng cung cấp có thể khác `story-N`; dùng đường dẫn rõ ràng đó.
2. Đọc tiêu đề, `Chủ đề:`, thân truyện, lời thoại và `Bài học cho bé`.
3. Lập danh sách nhân vật thực tế. Đọc mô tả và xem refs để viết mô tả chốt tiếng Anh. Với nhân vật mới thiếu thông tin cần thiết, hỏi gộp: loài, giới tính/tuổi, ngoại hình/trang phục, vai trò. Tiếp tục phần không phụ thuộc câu trả lời.
4. Chia khoảng 8–11 cảnh nội dung, thêm cover và infographic kết; điều chỉnh số cảnh theo độ dài truyện. Các nhịp thường gồm mở đầu, sự việc, phản ứng, lựa chọn, hành động, hỗ trợ, kết quả và bài học. Không bịa thêm tình tiết.
5. Lập bảng scene ↔ nhân vật, đánh dấu `(bg)` cho nhân vật xa. Tên cột lấy từ truyện hiện tại.
6. Viết `image-prompts-plan.md` theo cấu trúc dưới đây. Mỗi prompt đầy đủ độc lập, có refs và mô tả chốt tương ứng.
7. Báo đường dẫn, số ảnh, nhân vật và refs còn thiếu. Nếu người dùng chỉ sửa scene X thì sửa đúng phần đó, giữ các scene còn lại.

## Cấu trúc output

```markdown
# Plan tạo ảnh AI: "[Tên truyện]"

## Tổng quan
- Chủ đề: [chủ đề]
- Số ảnh: 1 cover + [K] cảnh nội dung + 1 infographic
- Khổ: dọc 5:7, safe margin cho A5
- Phong cách: [mô tả lấy từ yêu cầu/refs]
- Refs: [danh sách, đánh dấu ref thiếu]

## Quy tắc bắt buộc của truyện này
[Quy tắc danh tính, tỉ lệ, giải phẫu, trang phục và chữ dựa trên dữ liệu hiện tại]

## Quy trình thực hiện
### Bước 1: Chuẩn bị reference characters
[Link refs thực có, đường dẫn tương đối từ thư mục truyện]
### Bước 2: Mô tả chốt / character sheet
[Mô tả tiếng Anh cho mỗi nhân vật; prompt sheet cho ref thiếu]
### Bước 3: Tạo từng scene
Upload đúng refs → copy toàn bộ prompt → tạo ảnh → kiểm tra.

## Bảng tra cứu refs
| Scene | [Nhân vật A] | [Nhân vật B] |
|-------|:------------:|:------------:|
| 0 — Cover | [ref] | [ref] |

## Prompt chi tiết
### SCENE 0 — COVER
Mục đích: [giới thiệu chủ đề]
Refs: [danh sách]
[Một đoạn prompt tiếng Anh hoàn chỉnh, yêu cầu chữ tựa truyện chính xác]

### SCENE 1 — [Tên cảnh]
Bối cảnh: [1–2 câu tiếng Việt]
Refs: [danh sách]
[Một đoạn prompt tiếng Anh hoàn chỉnh]

[Lặp các scene tiếp theo]

### SCENE [K+1] — Bài học kết (Infographic)
Refs: [nhân vật có mặt]
[Prompt tiếng Anh; nội dung bài học đúng truyện; cho phép chữ tiếng Việt]

## Tips và thứ tự tạo
[Khoá nhân vật → cover → cảnh đông nhất → các cảnh còn lại → infographic]

## Checklist
- [ ] Ref/character sheet cần thiết
- [ ] Cover
- [ ] Từng scene nội dung
- [ ] Infographic
- [ ] Đúng số nhân vật, tỉ lệ, trang phục, chữ và phong cách
```

## Cấu trúc prompt

Mỗi scene là **một đoạn tiếng Anh** chứa lần lượt:

1. Nhân vật, hành động, cảm xúc, tư thế và hướng nhìn; lần đầu nhắc có đủ mô tả chốt.
2. Bối cảnh và ánh sáng phù hợp cảm xúc, không quá đáng sợ với độc giả nhỏ tuổi.
3. Bố cục dọc, góc camera, chiều sâu và hướng di chuyển nếu có.
4. Giải phẫu/thiết kế vật thể cần giữ theo tài liệu hiện tại.
5. Chữ được phép và chữ cần chặn; ghi chính xác tiêu đề/bảng tên khi cần.
6. Khớp refs: same face, same outfit, same proportions và các dấu hiệu nhận dạng cụ thể.
7. Style Bible của dự án, lặp cùng một mô tả xuyên suốt truyện; thêm `vertical 5:7 portrait page layout with safe margins for print, no important details near edges`.
8. Với tool hỗ trợ: `--ar 5:7 --style raw`; thêm negative prompt đúng scene. Cover bỏ cấm captions nếu cản tựa truyện; infographic không cấm chữ.

Character sheet cần front, 3/4 và side view, nền đơn giản, thiết kế và tỉ lệ nhất quán với phong cách dự án, khung vuông.

Flashback dùng bố cục phần trên hoặc viền phân biệt khi cần; nếu dùng thought bubble có chủ đích thì bỏ cấm tương ứng. Cảnh lo lắng có thể dùng tông lạnh dịu, đoàn tụ dùng màu ấm. Infographic dùng nền thoáng, ô pastel và chữ dễ đọc. Giữ nội dung bài học bằng tiếng Việt.

Ảnh xem trên màn hình có thể tạo thử chất lượng thấp với ref nhỏ. Khi in A5, dùng 300 DPI trở lên, tối thiểu khoảng 1748 × 2480 px; kiểm tra crop vì tỉ lệ in A5 khác nhẹ 5:7. Không tạo ảnh độ phân giải cao khi chưa có nhu cầu.
