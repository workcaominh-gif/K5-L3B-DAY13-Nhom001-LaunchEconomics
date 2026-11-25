# Báo cáo cá nhân — Hoàng Nhật Minh - 2A202603992

## 1. Thông tin thành viên

- Họ tên: Hoàng Nhật Minh
- MSSV: 2A202603992
- Email:
- Vai trong nhóm: Người viết code sau giờ giải lao (CP4 · Nhiệm vụ D)

## 2. Phần việc phụ trách

- Nhiệm vụ D (CP4): tính cỡ mẫu D1 trong `src/lab13.py`, trả lời năm câu D2, tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại và điền toàn bộ `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Viết `co_mau(p1, p2)` (cỡ mẫu mỗi nhóm khi so hai tỉ lệ, z chính xác 1,95996 và 0,84162), `he_so_thiet_ke(m)` (DE = 1 + (m − 1) × ICC) và `m_toi_thieu(n, c)` (giải 20m / (0,98 + 0,02m) ≥ 859 ra m nhỏ nhất).
- Viết `in_d1_co_mau`, in đủ năm câu D1:
  - a) Chia theo yêu cầu: 1.251 yêu cầu mỗi nhóm.
  - b) Theo nhân viên, m = 75: DE 2,48, cần 3.103 mỗi nhóm = 42 người/nhóm; tổng 84 > 40 nhân viên nên không đủ người.
  - c) 20 nhân viên mỗi nhóm: tối đa 20 / 0,02 = 1.000 < 1.251, không đạt.
  - d) 6 depot mỗi nhóm: tối đa 300, không đạt.
  - e) Mức chênh 6 điểm: 859 mỗi nhóm, cần m ≥ 299 yêu cầu/người, DE 6,96.
- Tính thêm con số bất lợi bằng statsmodels `NormalIndPower`: nếu tác động thật chỉ +5 điểm thì với n = 859 mỗi nhóm, power chỉ còn khoảng 0,64.
- Viết `in_d3_ti_le_mo_lai`: tỉ lệ mở lại 7 ngày hiện tại là 4,25% (51/1.200) trên toàn mẫu và 3,97% (39/982) trong phạm vi `noi_dia` + `hang_nang`. Vì vậy không đặt ngưỡng tuyệt đối 3% (pilot sẽ dừng ngay tuần đầu); luật an toàn so với nhóm đối chứng (chênh ≥ 2 điểm) kèm trần tuyệt đối 6%.
- Chọn cách chia theo nhân viên 20 + 20 (đủ 20 cụm mỗi nhóm, tách được tác động), chấp nhận đánh đổi mde 0,06 và ghi rõ trong phần chú thích đầu file.
- Điền `pilot_plan.yaml`:
  - phạm vi `noi_dia` + `hang_nang`, có số lấy từ bảng A3;
  - phần `identifiability`;
  - ba luật dừng (an toàn, chi phí, mức sử dụng), mỗi luật đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ và có vai trò được quyền dừng;
  - cách rollback;
  - ngày quyết định;
  - danh sách `simulated_inputs`.

## 4. Bằng chứng

- Commit `668ac05`: "feat(CP4): cỡ mẫu D1 và pilot_plan.yaml".
- `cd src && python lab13.py` in mục `D1 · Cỡ mẫu` và `D3 · Tỉ lệ hiện tại để đặt luật dừng`.
- `report/team/pilot_plan.yaml`:
  - `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi;
  - `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì;
  - lệnh `grep -rni` tìm từ cấm trong `report/team` (CHECKPOINTS.md, CP5) không in gì.

## 5. Công cụ AI đã dùng

- Dùng Claude (Claude Code) để viết các hàm D1 theo công thức trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, soạn nội dung `pilot_plan.yaml`, rồi commit và push.
- Cách tự kiểm tra:
  - chạy `python lab13.py`, so từng số D1 với bảng đối chiếu trong hướng dẫn: 1.251 · 3.103/42 người · 1.000 · 300 · m ≥ 299, DE 6,96, đều khớp;
  - giải tay câu e: 20m ≥ 859 × (0,98 + 0,02m) → 2,82m ≥ 841,82 → m ≥ 299;
  - kiểm tra file YAML bằng ba lệnh ở mục 4.
- Không dùng AI để bịa số. Tỉ lệ mở lại và chỉ số chính do code tính trực tiếp từ `logix_requests.csv`. Các ngày (bắt đầu 2026-12-07, quyết định 2027-01-05) và seed bốc thăm là giả định của nhóm.

## 6. Tự đánh giá

- CP4 đạt các điều kiện "Tự kiểm tra": năm câu D1 khớp đáp án, file YAML đọc được, không còn dấu `?`, có ba luật dừng đủ bốn vế, cách chia có đúng 20 cụm mỗi nhóm và đã ghi rõ đánh đổi.
- Điểm cần nói rõ với hội đồng: pilot chỉ đủ power cho mức chênh từ 6 điểm. Nếu tác động thật là 5 điểm thì power chỉ còn khoảng 0,64.
