# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: **Nguyễn Khắc Bào** (`2A202604072`) · Người gắn nhãn 2: **Vũ Văn Trường** (`2A202603910`) — gắn độc lập trong 8 phút, không trao đổi, giữ nguyên nhãn gốc sau khi so.

*Quy ước viết tắt ở cột Nhãn người 2 (giữ nguyên bản gốc commit `3141cd7`):* `ND` = Do người dùng · `HT` = Hệ thống · `NC` = Ngữ cảnh · `GH` = Giới hạn hệ thống · `NG` = Ngầm.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ND | Có | Do người dùng |
| 2 | Hệ thống | HT | Có | Hệ thống |
| 3 | Ngữ cảnh | NC | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | GH | Có | Giới hạn hệ thống |
| 5 | Ngầm | NG | Có | Ngầm |
| 6 | Do người dùng | ND | Có | Do người dùng |
| 7 | Hệ thống | HT | Có | Hệ thống |
| 8 | Hệ thống | HT | Có | Hệ thống |
| 9 | Do người dùng | ND | Có | Do người dùng |
| 10 | Ngữ cảnh | NC | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | GH | Có | Giới hạn hệ thống |
| 12 | Ngầm | NG | Có | Ngầm |
| 13 | Giới hạn hệ thống | GH | Có | Giới hạn hệ thống |
| 14 | Do người dùng | ND | Có | Do người dùng |
| 15 | Hệ thống | HT | Có | Hệ thống |
| 16 | Ngữ cảnh | NC | Có | Ngữ cảnh |
| 17 | Ngầm | NG | Có | Ngầm |
| 18 | Ngữ cảnh | NC | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | GH | Có | Giới hạn hệ thống |
| 20 | Hệ thống | HT | Có | Hệ thống |

**Tỉ lệ đồng thuận:** **20 / 20 = 100%** (đạt ngưỡng ≥ 80%).

**Phân bổ 20 ca theo 5 loại:** Do người dùng (**4**: ca 1, 6, 9, 14) · Hệ thống (**5**: ca 2, 7, 8, 15, 20) · Ngữ cảnh (**4**: ca 3, 10, 16, 18) · Giới hạn hệ thống (**4**: ca 4, 11, 13, 19) · Ngầm (**3**: ca 5, 12, 17).

## Quy tắc phân biệt cho các ca không trùng

Không có ca không trùng (đồng thuận 20/20 = 100%). Nhóm ghi lại các quy tắc phân biệt theo nguyên nhân gốc cho các ca dễ lẫn để dùng thống nhất khi vận hành pilot:

- **Ca 6, 9 là Do người dùng, không phải Hệ thống:** gốc lỗi là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý là điểm cần cải thiện ở cột khắc phục.
- **Ca 13 là Giới hạn hệ thống:** yêu cầu ngoài phạm vi sản phẩm luôn thuộc giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** lỗi sai đã lộ ra (trích dẫn bịa nhìn thấy được, nhân viên xem lại bắt được); nhãn Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra mẫu.
- **Ca 18 là Ngữ cảnh:** số tiền tính đúng chính sách, chỉ giả định "khách tự hiểu cách tính" không khớp hoàn cảnh của khách.
- **Ca 12 là Ngầm:** câu trả lời vẫn đúng nhưng chi phí token gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí chứ không chỉ sai câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được (gồm event/phương pháp đối soát, ngưỡng và tần suất). Người phụ trách là một vai trò có quyền quyết định, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` gắn `trace_id`; cảnh báo khi vượt **2% tổng yêu cầu/ngày** | Nhận diện định dạng mã sàn TMĐT và tự tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát **mỗi giờ** giữa tin nhắn "đã hoàn" và event `refund_ledger_write` (trạng thái `ok`) theo cùng `trace_id`; **ngưỡng 0 ca** | Chỉ báo "đã hoàn" khi sổ cái trả `ok`; lỗi 503 sau 3 lần thử thì báo "đang xử lý" và chuyển nhân viên kèm `trace_id` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` có lý do "sai số tiền" nhưng đối chiếu tính đúng; đo **hằng tuần**, cảnh báo khi **> 1% tổng đơn hoàn** | Chuẩn hoá mẫu tin nhắn luôn ghi rõ phép tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) và kênh nhận tiền | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` phân theo cột `loai`; đo **hằng tuần**, cảnh báo khi **> 5% yêu cầu trong phạm vi pilot** | Giữ cơ chế chuyển nhân viên kèm tóm tắt ngữ cảnh; loại `quoc_te` khỏi phạm vi pilot (đồng bộ CP1 và CP4) | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm tra mẫu ngẫu nhiên **100 đơn/tuần** so với bảng giá hiện hành; cảnh báo khi **> 1% đơn lệch** | Tự động xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi phiên bản bảng giá vào mọi `trace_id` | Kế toán trưởng |
