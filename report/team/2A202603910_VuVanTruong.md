# Báo cáo cá nhân — Vũ Văn Trường - 2A202603910

## 1. Thông tin thành viên

- Họ tên: Vũ Văn Trường
- MSSV: 2A202603910
- Email: tini.vu.0@gmail.com
- Vai trong nhóm: Người kiểm số (phụ trách CP2 · Nhiệm vụ B; kiêm viết code phần độ nhạy)

## 2. Phần việc phụ trách

- Nhiệm vụ B (CP2) — Bảng độ nhạy: viết các hàm tính độ nhạy trong `src/lab13.py`, điền toàn bộ bảng B1–B4 và câu trả lời B3, B4 vào `report/team/bang_chi_phi.md`.
- Đối chiếu số với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` và kiểm tra chéo bằng cách tính lại từ hai file CSV gốc.

## 3. Đóng góp cụ thể

- Viết `KICH_BAN_B1` với 9 kịch bản, mỗi kịch bản chỉ đổi đúng một yếu tố so với kết quả A2: giá token gấp đôi (52/260 đ) và giảm một nửa (13/65 đ), tiền xem lại ×2 và ÷2, tiền làm lại ×2 và ÷2, lương 2.500 đ/phút, giới hạn 2 lần và 1 lần chạy.
- Viết `in_b1_do_nhay`: gọi lại `mo_hinh` cho từng kịch bản, in chi phí mỗi việc thành công và phần trăm thay đổi so với mốc 4.472 đ; thêm câu tự kiểm tra dạng `assert` rằng kịch bản "giảm một nửa" phải bằng đúng −½ kịch bản "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).
- Viết `in_b2_cap`: kịch bản đổi cặp giá token ×2 cùng tỉ lệ xem lại ×2 cho 6.543 đ (+46,3%), đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính; xếp hạng ba yếu tố mạnh nhất: 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên.
- Viết `in_b3_gioi_han`: chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Kết quả: 1 lần → 7.449.781 đ; 2 lần → 6.901.220 đ (rẻ nhất cho công ty); 3 lần → 7.037.585 đ. Giới hạn rẻ nhất không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ), vì chọn 1 lần đẩy thêm 85 việc sang nhân viên.
- Viết `in_b4_xem_lai_tat_ca`: phạm vi `noi_dia` + `hang_nang` gồm 982 yêu cầu, trong đó 948 yêu cầu có lần chạy `ok` được xem lại 5 phút, 48 ca làm lại, token+tool 224.513 đ. Với 9 phút/ca: tổng 10.568.513 đ ÷ 900 việc thành công = 11.743 đ = 0,98× baseline. Với 15,3 phút/ca (trung bình trong dữ liệu): 12.415 đ = 1,03×. Tính thêm mức hoà vốn: mỗi lần xem lại phải ≤ 5,1 phút (hoặc ≤ 4,8 phút nếu làm lại 15,3 phút). Kết luận: tiền xem lại chiếm ~90% chi phí nên pilot phải học cách giảm tỉ lệ xem lại và độ dài mỗi lần xem lại.
- Điền B1 (đủ 9 dòng), B2 (cặp + xếp hạng), B3 và B4 vào `report/team/bang_chi_phi.md`; gắn nhãn `simulated` ở mọi dòng tính từ `phut_xem_lai_simulated` / `phut_lam_lai_simulated` và giữ mỗi câu trả lời không quá ba dòng, có số.

## 4. Bằng chứng

- Commit `c1d9d15` — "feat(CP2): bảng độ nhạy B1-B4" (15:17:48 GMT+7), gồm `src/lab13.py` (+96 dòng) và `report/team/bang_chi_phi.md` (điền 34 dòng).
- `cd src && python lab13.py` chạy trọn vẹn, exit code 0, in `Tự kiểm tra "giảm một nửa = −½ gấp đôi": ĐẠT`.
- `report/team/bang_chi_phi.md`, mục B1 (9 dòng), B2, B3 (bảng 3 giới hạn) và B4.
- Kiểm tra chéo độc lập: tự tính lại từng số B1–B4 trực tiếp từ `logix_runs.csv` và `logix_requests.csv` (không dùng lại hàm `mo_hinh`), mọi con số đều khớp với báo cáo và với bảng đáp án trong hướng dẫn chi tiết.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI để viết các hàm `in_b1_do_nhay`, `in_b2_cap`, `in_b3_gioi_han`, `in_b4_xem_lai_tat_ca`, soạn nội dung bảng B1–B4 và kiểm tra commit/pull.
- Cách tự kiểm tra: (1) chạy `python lab13.py` và đối chiếu từng số in ra với bảng đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; (2) câu `assert` trong code tự kiểm tra tính đối xứng "gấp đôi / giảm một nửa"; (3) tính lại độc lập từ hai file CSV gốc để chắc rằng số trong báo cáo không phải do AI bịa ra.
- Không dùng AI để bịa số hay nhãn: mọi con số đều do `src/lab13.py` tính trực tiếp từ dữ liệu giả lập, và các dòng từ cột `_simulated` đều có nhãn `simulated`.

## 6. Tự đánh giá

- CP2 hoàn thành đúng điều kiện "Xong khi": bảng B1 đủ 9 dòng, có xếp hạng ba yếu tố, B3 và B4 mỗi câu có số và không quá ba dòng; tự kiểm tra đạt; số khớp đáp án trong ngưỡng 2% của rubric C2.
- Điểm cần lưu ý khi bảo vệ: với mức chênh thật chỉ 5 điểm thì pilot chỉ có power khoảng 0,64 (con số bất lợi đã được ghi trong CP4), và xem lại 100% gần như không tiết kiệm so với nhân viên tự làm (11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× nếu làm lại đúng 15,3 phút như dữ liệu).
- Còn cần làm: cập nhật dòng thông tin của mình vào `TEAM.md`, hoàn thiện CP3/CP5 theo phân vai và commit/push báo cáo cá nhân này cùng commit chốt của nhóm.
