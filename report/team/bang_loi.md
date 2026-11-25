# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... (chờ người bạn cùng nhóm tự gắn) · Người gắn nhãn 2: Vũ Văn Trường (bản nháp để duyệt)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ND | ... | ... |
| 2 | ... | HT | ... | ... |
| 3 | ... | NC | ... | ... |
| 4 | ... | GH | ... | ... |
| 5 | ... | NG | ... | ... |
| 6 | ... | ND | ... | ... |
| 7 | ... | HT | ... | ... |
| 8 | ... | HT | ... | ... |
| 9 | ... | ND | ... | ... |
| 10 | ... | NC | ... | ... |
| 11 | ... | GH | ... | ... |
| 12 | ... | NG | ... | ... |
| 13 | ... | GH | ... | ... |
| 14 | ... | ND | ... | ... |
| 15 | ... | HT | ... | ... |
| 16 | ... | NC | ... | ... |
| 17 | ... | NG | ... | ... |
| 18 | ... | NC | ... | ... |
| 19 | ... | GH | ... | ... |
| 20 | ... | HT | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...% (chờ bộ nhãn người 1 để so)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 6, 9 là do người dùng, không phải hệ thống:** gốc lỗi là khách chọn sai mục hoặc nhập sai mã. Việc trợ lý không gợi ý là việc cần cải thiện, nằm ở cột khắc phục.
- **Ca 13 là giới hạn:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.
- **Ca 8, 15 là hệ thống, không phải ngầm:** sai đã lộ ra (trích dẫn nhìn thấy được, nhân viên bắt được). Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- **Ca 18 là ngữ cảnh:** số tiền đúng chính sách, chỉ giả định "khách hiểu cách tính" là không khớp.
- **Ca 12 là ngầm:** kết quả vẫn đúng nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí, không chỉ về câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá 2% số yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi sổ cái ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ mở lại vì số tiền mà kiểm tra thấy đúng, theo tuần | Mẫu tin nhắn luôn ghi cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = `thieu_du_lieu`, theo loại yêu cầu | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
