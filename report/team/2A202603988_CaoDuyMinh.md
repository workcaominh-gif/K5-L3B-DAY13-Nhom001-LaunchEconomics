# Báo cáo cá nhân — Cao Duy Minh - 2A202603988

## 1. Thông tin thành viên

- Họ tên: Cao Duy Minh
- MSSV: 2A202603988
- Email:
- Vai trong nhóm: Người viết code (CP1)

## 2. Phần việc phụ trách

- Nhiệm vụ A (CP1): viết `src/lab13.py` — mô hình chi phí mỗi việc thành công từ trace, tách theo loại yêu cầu, cộng chi phí cố định.
- Fork và đổi tên repo nhóm, dựng `TEAM.md` ban đầu.

## 3. Đóng góp cụ thể

- Viết ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) theo đúng công thức kỳ vọng số lần chạy và tỉ lệ thành công; cả ba phép thử đáp án biết trước đều đạt (1,20 · 1,25 · 1,25).
- Viết `mo_hinh(runs, reqs, ...)` (A2): cộng tiền token + tool trên mọi lần chạy (kể cả lỗi), cộng tiền xem lại/làm lại từ hai cột `_simulated`, chia cho số yêu cầu có `ket_qua == 'thanh_cong'`. Giữ tham số giá/hệ số/`max_lan_chay` sẵn cho Nhiệm vụ B.
- Viết `in_bang_a3`: gọi lại `mo_hinh` lọc theo từng giá trị cột `loai` (A3).
- Viết `in_a4_chi_phi_co_dinh`: cộng chi phí cố định 40 triệu đ/tháng vào chi phí mỗi việc thành công, phạm vi `noi_dia` + `hang_nang`, ở hai mức khối lượng (45.000 và một nửa).
- Đối chiếu từng con số đầu ra với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` — khớp tuyệt đối, không lệch (A2: cps = 4.472 đ; A3: bốn dòng theo loại; A4: 4.599 đ và 5.784 đ).
- Điền bảng A1–A4 trong `report/team/bang_chi_phi.md` bằng đúng số do code in ra, giữ nhãn `simulated` ở các dòng tính từ `phut_xem_lai_simulated` / `phut_lam_lai_simulated`.

## 4. Bằng chứng

- Commit `ee8749b` — "feat(CP1): mô hình chi phí mỗi việc thành công (A1-A4)".
- `src/lab13.py` chạy `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` rồi bảng A2, A3, A4.
- `report/team/bang_chi_phi.md`, mục A1–A4.

## 5. Công cụ AI đã dùng

- Dùng Claude (Claude Code) để viết code `src/lab13.py` theo khung và công thức có sẵn trong đề bài (`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`), và để fork/đổi tên repo, commit, push.
- Tự kiểm tra bằng cách chạy `python lab13.py` và so từng số (A2, A3, A4) với bảng đáp án đối chiếu trong tài liệu hướng dẫn chi tiết — mọi số khớp trong sai số cho phép (≤ 2%), không có số lệch.
- Không dùng AI để bịa số: mọi con số đều do `src/lab13.py` tính trực tiếp từ `logix_runs.csv` / `logix_requests.csv`.

## 6. Tự đánh giá

- Hoàn thành phần Nhiệm vụ A (CP1) đúng công thức, ba phép thử đạt, số A2–A4 khớp đáp án đối chiếu.
- Còn lại: điền đủ thông tin cá nhân (email, MSSV các thành viên khác), và các checkpoint B–E cần làm nhóm theo phân vai trong `TEAM.md`.
