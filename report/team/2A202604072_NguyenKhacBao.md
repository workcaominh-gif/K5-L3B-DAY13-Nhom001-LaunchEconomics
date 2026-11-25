# Báo cáo cá nhân — Nguyễn Khắc Bào - 2A202604072

## 1. Thông tin thành viên

- Họ tên: Nguyễn Khắc Bào
- MSSV: 2A202604072
- Email: baonk.invzble.z@gmail.com
- Vai trong nhóm: Người gắn nhãn 1 (CP3 · Nhiệm vụ C)

## 2. Phần việc phụ trách

- Nhiệm vụ C (CP3) — Bảng lỗi và cách khắc phục: gắn nhãn độc lập 20 ca lỗi theo năm loại của Google PAIR (**Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**), so nhãn và tính tỉ lệ đồng thuận với Người gắn nhãn 2 (Vũ Văn Trường), rà soát quy tắc phân biệt các ca dễ lẫn và hoàn thiện bảng khắc phục 5 ca đại diện trong `report/team/bang_loi.md`.
- Cập nhật Mục 5 (*Bảng lỗi và cách khắc phục*) trong `report/team/ho_so_launch_v0.md` và cập nhật phần thông tin/đóng góp trong `TEAM.md`.

## 3. Đóng góp cụ thể

- Đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và rà duyệt bộ nhãn độc lập của Người gắn nhãn 1 theo nguyên tắc phân loại **theo nguyên nhân gốc, không theo chỗ cần sửa**.
- Phối hợp với Vũ Văn Trường (Người gắn nhãn 2, commit `3141cd7`), giữ nguyên bộ nhãn độc lập của hai người và tính tỉ lệ đồng thuận: **20/20 = 100%** (vượt ngưỡng tối thiểu 80% của Rubric C3).
  - Phân bổ 20 ca: Do người dùng (**4**: ca 1, 6, 9, 14) · Hệ thống (**5**: ca 2, 7, 8, 15, 20) · Ngữ cảnh (**4**: ca 3, 10, 16, 18) · Giới hạn hệ thống (**4**: ca 4, 11, 13, 19) · Ngầm (**3**: ca 5, 12, 17).
- Chốt các quy tắc phân biệt cho các ca dễ lẫn (`6, 9` thuộc Do người dùng; `13` thuộc Giới hạn hệ thống; `8, 15` thuộc Hệ thống chứ không phải Ngầm; `18` thuộc Ngữ cảnh; `12` thuộc Ngầm về chi phí).
- Hoàn thiện bảng khắc phục cho 5 ca đại diện đủ 5 loại (`ca 9, 7, 18, 4, 17`), chuẩn hoá mọi dòng đều có:
  - cách phát hiện **đo được** gồm tên event/phương pháp đối soát gắn `trace_id`, ngưỡng cảnh báo và tần suất (`input_validation_failed` > 2%/ngày; đối soát `refund_ledger_write` mỗi giờ ngưỡng 0 ca; `ticket_reopened` hằng tuần > 1%; `handoff_to_staff` hằng tuần > 5%; `audit_sample_checked` 100 đơn/tuần > 1%);
  - giải pháp khắc phục đúng nguyên nhân gốc và đồng bộ phạm vi pilot (`loại quoc_te`) với CP1 & CP4;
  - **một vai trò phụ trách** cụ thể (*PM trợ lý hoàn phí*, *Kỹ sư trưởng agent*, *Trưởng nhóm CSKH*, *Kế toán trưởng*), không ghi "cả đội".
- Cập nhật Mục 5 trong `report/team/ho_so_launch_v0.md` (trạng thái `Xong, có bằng chứng`) và kiểm tra toàn thư mục `report/team/` không chứa từ cấm theo `RULES.md`.

## 4. Bằng chứng

- `report/team/bang_loi.md`: đủ 2 bộ nhãn độc lập (Nguyễn Khắc Bào và Vũ Văn Trường), tỉ lệ đồng thuận 20/20 (100%), quy tắc phân biệt ca dễ lẫn và bảng khắc phục 5 ca đủ 5 loại.
- `report/team/ho_so_launch_v0.md`: Mục 5 đã điền số liệu chính, trạng thái `Xong, có bằng chứng` và vai trò phụ trách.
- `TEAM.md`: cập nhật thông tin thành viên dòng 3 và mục đóng góp `NguyenKhacBao-2A202604072`.
- Kết hợp với commit `3141cd7` (nhãn độc lập Người gắn nhãn 2 của Vũ Văn Trường).

## 5. Công cụ AI đã dùng

- Dùng Antigravity (Gemini) để rà soát tiến độ repo, lập kế hoạch CP3, phân tích nguyên nhân gốc cho 20 ca lỗi để tự duyệt, chuẩn hoá event/ngưỡng/tần suất trong bảng khắc phục 5 ca và soát lỗi trình bày theo checklist.
- Cách tự kiểm tra:
  - tự đọc mô tả từng ca trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và rà lại từng ca dễ lẫn (`6, 8, 9, 12, 13, 15, 18`) trước khi chốt duyệt;
  - giữ nguyên bộ nhãn độc lập do Vũ Văn Trường push ở commit `3141cd7`, đối chiếu trực tiếp 20/20 dòng và so khớp với bảng tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`;
  - kiểm tra đủ 5 loại ở bảng khắc phục, đủ event + ngưỡng + tần suất, không có vai trò "cả đội" và chạy kiểm tra từ cấm trên `report/team/`.

## 6. Tự đánh giá

- CP3 đạt đầy đủ tiêu chí Rubric C3 (10/10): hai bộ nhãn độc lập giữ nguyên, đồng thuận 20/20 (100% ≥ 80%), khớp đáp án 20/20 (≥ 16/20), bảng khắc phục đủ 5 loại với cách đo cụ thể và vai trò rõ ràng, sẵn sàng ghép vào CP5 (`chi_so.md` và `ho_so_launch_v0.md`).
- Điểm cần nhóm tiếp tục phối hợp: tổng hợp đầy đủ 7 mục trong `ho_so_launch_v0.md`, hoàn thiện `chi_so.md` (dùng lại các event đã đặt tên trong `bang_loi.md`), `group_report.md` và duyệt chéo Gate 2a (`phieu_cham.md`).
