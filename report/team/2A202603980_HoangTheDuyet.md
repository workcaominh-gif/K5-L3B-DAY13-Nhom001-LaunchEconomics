# Báo cáo cá nhân — Hoàng Thế Duyệt - 2A202603980

## 1. Thông tin thành viên

- Họ tên: Hoàng Thế Duyệt
- MSSV: 2A202603980
- Email:
- GitHub: `theduythg`
- Vai trong nhóm: Người giữ hồ sơ & tổng hợp CP5 (Nhiệm vụ E)

## 2. Phần việc phụ trách

- Nhiệm vụ E (CP5): hoàn thiện `report/team/chi_so.md` (đặc tả chỉ số E1, danh sách event có `trace_id`, rủi ro kinh tế E2), tổng hợp hồ sơ một trang `report/team/ho_so_launch_v0.md` (ghép kết quả CP1–CP4 và chốt đề xuất Gate 2a), hoàn thiện `report/team/group_report.md`, cập nhật `report/team/phieu_cham.md`, bổ sung hàm `in_e1_chi_so` trong `src/lab13.py` và rà soát checklist nộp bài.

## 3. Đóng góp cụ thể

- Bổ sung hàm `in_e1_chi_so(reqs)` trong `src/lab13.py` để tính và in trực tiếp 3 chỉ số E1 trên 1.200 yêu cầu:
  - Chính (`dong_trong_24h == 1` & `mo_lai_trong_7_ngay == 0`): **82,83%** (994/1.200).
  - Dùng (`quyet_dinh_xem_lai` là `sua` hoặc `bo` trên `duoc_xem_lai == 1`): **27,12%** (48/177).
  - An toàn (`mo_lai_trong_7_ngay == 1`): **4,25%** (51/1.200).
- Hoàn thiện `report/team/chi_so.md`:
  - Đủ 3 chỉ số bắt buộc + 2 chỉ số tự đề xuất (tỉ lệ giữ gợi ý của nhân viên; % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần).
  - Liệt kê 10 event đều có `trace_id` kèm mục kiểm tra chéo chứng minh cả 5 chỉ số đều đo được.
  - Bảng E2 gồm 3 dòng rủi ro kinh tế lấy số trực tiếp từ `report/team/bang_chi_phi.md` (làm lại ×2, xem lại 100% kéo dài, khối lượng thấp hơn dự kiến), có nhãn `simulated`, ngưỡng theo dõi, hành động và một vai trò phụ trách.
- Hoàn thiện `report/team/ho_so_launch_v0.md`:
  - Điền đủ 7 mục (giữ nguyên Mục 5 từ CP3), ghi đúng cột trạng thái và một vai trò phụ trách mỗi mục.
  - Chốt đề xuất **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang`, nêu rõ các con số bất lợi (xem lại 100% tốn 0,98×–1,03× `simulated`; power ~0,64 ở +5 điểm) kèm 4 điều kiện có người phụ trách và ngày kiểm tra.
- Hoàn thiện `report/team/group_report.md` (mục 1–8) và ghi nhận trạng thái chưa phân cặp duyệt chéo Gate 2a trong `report/team/phieu_cham.md`.

## 4. Bằng chứng

- Commit `6d9153f` ("feat(CP5): chỉ số E1, rủi ro E2, hồ sơ launch v0 và báo cáo nhóm").
- `src/lab13.py`: chạy `src\.venv\Scripts\python.exe lab13.py` trong `src/` đạt toàn bộ từ A1 đến E1 (`Ba phép thử đáp án biết trước: ĐẠT`, `Tự kiểm tra "giảm một nửa = −½ gấp đôi": ĐẠT`).
- `report/team/pilot_plan.yaml`: kiểm tra đọc thành công bằng `yaml.safe_load`.
- `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Antigravity / Gemini) để rà soát tiến độ các checkpoint CP1–CP4, hoàn thiện phần CP5 (`chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`, `in_e1_chi_so`) và kiểm tra checklist nộp bài.
- Cách tự kiểm tra:
  - Chạy trực tiếp `src/lab13.py` trong `src/.venv` để đối chiếu mọi con số E1 với `logix_requests.csv` và kiểm tra tính nhất quán với `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`.
  - Chạy `yaml.safe_load` kiểm tra `pilot_plan.yaml`, kiểm tra toàn bộ `report/team/` và `TEAM.md` không chứa từ cấm theo `RULES.md`, không ghi vai trò `"cả đội"` và mọi số từ `_simulated` đều có nhãn `simulated`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ các sản phẩm CP5 theo [CHECKPOINTS.md](../../CHECKPOINTS.md) và [RUBRIC.md](../../RUBRIC.md) (C5–C8): chỉ số E1 tính đúng từ dữ liệu, 10 event có `trace_id`, 3 dòng rủi ro có số từ bảng độ nhạy, hồ sơ launch v0 một trang 7 mục với đề xuất **Go có điều kiện** bám sát bằng chứng và nêu rõ con số bất lợi.
- Lưu ý: buổi lab chưa được Labcoach phân cặp duyệt chéo Gate 2a nên phần chấm nhóm khác trong `phieu_cham.md` giữ nguyên biểu mẫu và ghi chú rõ trạng thái, không tự điền số giả.
