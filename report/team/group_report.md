# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom001
- Lớp: L3B
- Thành viên: xem `TEAM.md` (4 thành viên, phân vai theo `TEAM.md`)

## 2. Mục tiêu và cách tiếp cận

Đánh giá trợ lý hoàn phí của LogiX-VN để ra quyết định tại Gate 2a: có nên mở pilot hay không. Nhóm dùng mẫu 1.200 yêu cầu / 1.624 lần chạy (dữ liệu giả lập) theo chuỗi: đo chi phí cho mỗi việc thành công → tìm yếu tố nhạy → phân loại lỗi → thiết kế pilot có đối chứng → đóng gói hồ sơ cho hội đồng. Mọi con số được `src/lab13.py` tính từ hai file CSV; riêng phút xem lại và phút làm lại lấy từ cột `_simulated` nên luôn gắn nhãn `simulated`.

## 3. Giải pháp

- **A — Mô hình chi phí** (`src/lab13.py`, `bang_chi_phi.md`): ba phép thử đạt 1,20 · 1,25 · 1,25; `mo_hinh` cộng token + tool trên mọi lần chạy kể cả lỗi, cộng giờ nhân viên, chia cho số việc thành công; tách 4 loại yêu cầu và cộng chi phí cố định 40 triệu/tháng.
- **B — Bảng độ nhạy** (`bang_chi_phi.md`): 9 kịch bản đổi một yếu tố, 1 kịch bản đổi cặp, 3 giới hạn số lần chạy với chi phí cả hệ thống, kịch bản xem lại 100%.
- **C — Bảng lỗi** (`bang_loi.md`): hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, đối chiếu 20/20, kèm 5 biện pháp khắc phục có event/ngưỡng và một vai trò phụ trách.
- **D — Pilot plan** (`pilot_plan.yaml`): tính 5 câu cỡ mẫu, chọn chia theo nhân viên 20 + 20, ghi rõ đánh đổi mde 0,06 và ba luật dừng bốn vế.
- **E — Chỉ số, rủi ro, hồ sơ** (`chi_so.md`, `ho_so_launch_v0.md`): ba chỉ số tính thử, 10 event có `trace_id`, kiểm tra chéo khả năng đo, ba dòng rủi ro lấy số từ bảng độ nhạy, đề xuất Go có điều kiện.

## 4. Kết quả

- CPS toàn mẫu 4.472 đ = 0,37× của 12.000 đ; phạm vi `noi_dia` + `hang_nang` 3.414 đ, cộng cố định 4.599 đ = 0,38× [simulated]. `quoc_te` 22.515 đ = 1,88× nên bị loại khỏi pilot.
- Yếu tố nhạy nhất: số ca làm lại +51,8% (6.787 đ), rồi tỉ lệ xem lại +40,7%; giá token chỉ +5,6% [simulated]. Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), nhưng CPS thấp nhất ở 1 lần (4.111 đ) [simulated]. Xem lại 100% cho 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút) [simulated].
- Chỉ số trong đợt chạy thử: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200). Chưa có đối chứng nên không kết luận trợ lý đã nâng chỉ số.
- Pilot: 20 nhân viên mỗi nhóm, 859 việc/nhóm (299 yêu cầu/người), mde 0,06; nếu tác động thật +5 điểm thì power ≈ 0,64. Ngày quyết định 2027-01-05.
- Đề xuất cuối trong `ho_so_launch_v0.md`: **Go có điều kiện** (bốn điều kiện về phạm vi, cỡ mẫu, luật dừng và thời gian xem lại).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: **chưa có** — `phieu_cham.md` là phiếu nhóm mình chấm nhóm khác, do hội đồng điền tại buổi duyệt, không do AI tạo theo `RULES.md`. Sẽ cập nhật khi nhận được phiếu.

## 5. Khó khăn và cách xử lý

- Đọc CSV với `keep_default_na=False`, nếu không ô trống ở `quyet_dinh_xem_lai` bị đọc thành `NaN` và làm sai tỉ lệ bỏ qua gợi ý.
- Phân biệt lỗi đã lộ ra (hệ thống) và lỗi ngầm: ca 12 có kết quả đúng nhưng tốn gấp 3 lần token suốt 3 tuần nên vẫn gắn nhãn ngầm; ca 8, 15 có sai lộ ra nên gắn hệ thống, không gắn ngầm.
- Cỡ mẫu: không cách chia theo cụm nào đủ cho +5 điểm (tối đa 1.000 < 1.251). Nhóm ghi rõ đánh đổi mde 0,06 và con số power 0,64 thay vì giả vờ đạt.
- Nhẩm lẫn dễ gặp: tối ưu CPS riêng lẻ cho giới hạn 1 lần nhưng làm cả hệ thống đắt hơn; đã sửa bằng cách tính thêm chi phí 12.000 đ cho mỗi việc chuyển nhân viên.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và bốn báo cáo cá nhân `report/team/*_*.md`.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu là giả lập và không có nhóm đối chứng: mọi kết luận về hiệu quả chỉ có thể đưa ra sau pilot, không phải từ đợt chạy thử này.
- Phút xem lại/làm lại là số giả lập; pilot phải thay bằng số đo được từ event `staff_review_decision` và `staff_rework_completed`.
- Pilot chỉ đủ power cho mức chênh từ 6 điểm; muốn phát hiện +5 điểm thì cần tăng số cụm hoặc chấp nhận power thấp hơn, được ghi rõ trong `pilot_plan.yaml`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com).
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (đề bài và hướng dẫn đối chiếu của lab).
