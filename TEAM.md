# Team

## Thông tin nhóm

- Tên nhóm: Nhom001
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom001-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/workcaominh-gif/K5-L3B-DAY13-Nhom001-LaunchEconomics · nhánh `main` · commit chốt = HEAD của `main` lúc nộp (`git log -1 --format=%h`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Cao Duy Minh | 2A202603988 | cduyminh@gmail.com | `workcaominh-gif` | Người viết code (CP1) |
|   2 | Hoàng Nhật Minh | 2A202603992 | minh40009@gmail.com | | Người viết code sau giải lao (CP4) |
|   3 | Nguyễn Khắc Bào | 2A202604072 | baonk.invzble.z@gmail.com | `invzble zone` | Người gắn nhãn 1 (CP3) |
|   4 | Vũ Văn Trường | 2A202603910 | tini.vu.0@gmail.com | `Sz3RO` | Người kiểm số (CP2), Người gắn nhãn 2 (CP3) |
|   5 | Hoàng Thế Duyệt | 2A202603980 | theduyethg05@gmail.com | `theduythg` | Người giữ hồ sơ & tổng hợp CP5 (Nhiệm vụ E) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## CaoDuyMinh-2A202603988

### Phần việc phụ trách

- CP1 · Nhiệm vụ A (Người viết code): xây dựng mô hình chi phí mỗi việc thành công từ trace trong `src/lab13.py`, điền bảng A1–A4 trong `report/team/bang_chi_phi.md`; fork repo và dựng `TEAM.md` ban đầu.

### Đóng góp cụ thể

- Viết ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`); cả ba phép thử đáp án biết trước đạt 1,20 · 1,25 · 1,25.
- Viết `mo_hinh(runs, reqs, ...)` (A2): cộng token + tool trên **mọi lần chạy kể cả lỗi**, cộng tiền xem lại/làm lại từ hai cột `_simulated`, chia cho số yêu cầu `ket_qua == 'thanh_cong'`; giữ sẵn tham số giá/hệ số/`max_lan_chay` để CP2 gọi lại.
- Viết `in_bang_a3` (A3: tách theo 4 loại yêu cầu) và `in_a4_chi_phi_co_dinh` (A4: cộng 40 triệu đ/tháng cho `noi_dia` + `hang_nang` ở hai mức khối lượng 45.000 và một nửa).
- Đối chiếu số in ra với hướng dẫn: A2 cps = 4.472 đ, A3 đủ 4 dòng theo loại, A4 = 4.599 đ và 5.784 đ — khớp đáp án, sai số 0%.
- Điền bảng A1–A4 vào `report/team/bang_chi_phi.md`, gắn nhãn `simulated` ở dòng tính từ phút xem lại/làm lại.

### Bằng chứng

- Commit `ee8749b` — "feat(CP1): mô hình chi phí mỗi việc thành công (A1-A4)" (2026-11-25 14:51:55), tác giả `cduyminh <cduyminh@gmail.com>`.
- Commit `5b314b3` — "docs: báo cáo cá nhân Cao Duy Minh (CP1)" (2026-11-25 14:56:18).
- `src/lab13.py`: `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`; `report/team/bang_chi_phi.md` mục A1–A4.
- Báo cáo cá nhân: `report/team/2A202603988_CaoDuyMinh.md`.

## HoangNhatMinh-2A202603992

### Phần việc phụ trách

- CP4 · Nhiệm vụ D: cỡ mẫu D1 trong `src/lab13.py`, năm câu D2 và toàn bộ `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Viết `co_mau`, `he_so_thiet_ke`, `m_toi_thieu`, `in_d1_co_mau`, `in_d3_ti_le_mo_lai` trong `src/lab13.py`.
- Kết quả D1:
  - chia theo yêu cầu: 1.251 mỗi nhóm;
  - theo nhân viên, m = 75: 3.103 mỗi nhóm = 42 người/nhóm, không đủ người;
  - 20 nhân viên mỗi nhóm: tối đa 1.000, không đạt;
  - 6 depot mỗi nhóm: tối đa 300, không đạt;
  - mức chênh 6 điểm: 859 mỗi nhóm, m ≥ 299, DE 6,96.
- Con số bất lợi: nếu tác động thật chỉ +5 điểm thì power khoảng 0,64.
- Chọn chia theo nhân viên 20 + 20, chấp nhận mde 0,06. Tính tỉ lệ mở lại 7 ngày hiện tại (4,25% toàn mẫu, 3,97% trong phạm vi) rồi mới đặt luật an toàn: so với đối chứng (chênh ≥ 2 điểm) kèm trần 6%.
- Viết ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, phần `identifiability`, `rollback`, `simulated_inputs`.

### Bằng chứng

- Commit `668ac05` ("feat(CP4): cỡ mẫu D1 và pilot_plan.yaml").
- Commit `8cd0ca7` ("HoangNhatMinh report") — thêm báo cáo cá nhân và cập nhật TEAM.md.
- `report/team/pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn dấu `?`, không có từ cấm theo RULES.md.
- Báo cáo cá nhân: `report/team/2A202603992_HoangNhatMinh.md`.

## NguyenKhacBao-2A202604072

### Phần việc phụ trách

- CP3 · Nhiệm vụ C: Người gắn nhãn 1 độc lập 20 ca lỗi theo 5 loại Google PAIR, đối chiếu đồng thuận với Người gắn nhãn 2 (Vũ Văn Trường), chốt quy tắc phân biệt và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`; cập nhật Mục 5 trong `report/team/ho_so_launch_v0.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập đủ 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` theo nguyên nhân gốc; so với bộ nhãn độc lập của Vũ Văn Trường (commit `3141cd7`) đạt đồng thuận **20/20 = 100%** (phân bổ: 4 Do người dùng, 5 Hệ thống, 4 Ngữ cảnh, 4 Giới hạn hệ thống, 3 Ngầm).
- Rà soát và hoàn thiện các quy tắc phân biệt ca dễ lẫn (ca 6, 8, 9, 12, 13, 15, 18) và chuẩn hoá đủ 5 dòng bảng khắc phục (ca 9, 7, 18, 4, 17) sao cho mỗi dòng đều có cách phát hiện đo được (event/đối soát, ngưỡng, tần suất) gắn `trace_id` và một vai trò phụ trách cụ thể.
- Cập nhật Mục 5 (*Bảng lỗi và cách khắc phục*) trong `report/team/ho_so_launch_v0.md` với trạng thái `Xong, có bằng chứng` và kiểm tra không dùng từ cấm theo `RULES.md`.

### Bằng chứng

- Commit `d2f3c58` — "feat(CP3): hoàn thiện bảng lỗi, bảng khắc phục 5 ca và mục 5 hồ sơ" (2026-11-25 16:31:57).
- Commit `15f757a` — "docs: báo cáo cá nhân Nguyễn Khắc Bào (CP3) và cập nhật TEAM.md" (2026-11-25 16:31:58).
- `report/team/bang_loi.md`: hai bộ nhãn độc lập, tỉ lệ đồng thuận 20/20 (100%), quy tắc phân biệt và bảng khắc phục 5 ca đủ 5 loại.
- `report/team/ho_so_launch_v0.md`: Mục 5.
- Báo cáo cá nhân: `report/team/2A202604072_NguyenKhacBao.md`.

## HoangTheDuyet-2A202603980

### Phần việc phụ trách

- CP5 · Nhiệm vụ E: hoàn thiện `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md` và bổ sung `in_e1_chi_so` trong `src/lab13.py`.

### Đóng góp cụ thể

- Bổ sung hàm `in_e1_chi_so(reqs)` trong `src/lab13.py` tính thử ba chỉ số E1 trên 1.200 yêu cầu: Chính **82,83%** (994/1.200), Dùng bỏ qua gợi ý **27,12%** (48/177), An toàn mở lại 7 ngày **4,25%** (51/1.200).
- Hoàn thiện `report/team/chi_so.md` (3 chỉ số tính thử + 2 chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo đo được cho cả 5 chỉ số, 3 dòng rủi ro kinh tế từ `bang_chi_phi.md` có nhãn `simulated`).
- Hoàn thiện 7 mục trong `report/team/ho_so_launch_v0.md` (giữ nguyên Mục 5 của CP3) với đề xuất **Go có điều kiện** kèm 4 điều kiện có người phụ trách, ngày kiểm tra và các con số bất lợi (xem lại 100% tốn 0,98×–1,03× `simulated`; power ~0,64 ở +5 điểm).
- Hoàn thiện `report/team/group_report.md` và ghi nhận trạng thái chưa phân cặp duyệt chéo Gate 2a trong `report/team/phieu_cham.md`.

### Bằng chứng

- Commit `6d9153f` ("feat(CP5): chỉ số E1, rủi ro E2, hồ sơ launch v0 và báo cáo nhóm").
- Commit `f01dfa4` ("docs(CP5): cập nhật TEAM.md, báo cáo cá nhân Hoàng Thế Duyệt và phiếu chấm") — tác giả `HoangDuyet2005 <theduyethg05@gmail.com>`.
- Commit `bbe9528` ("docs: hoàn tất thông tin nộp trong TEAM.md").
- `src/lab13.py`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`.
- Báo cáo cá nhân: `report/team/2A202603980_HoangTheDuyet.md`.

## VuVanTruong-2A202603910

### Phần việc phụ trách

- CP2 · Nhiệm vụ B (Người kiểm số): dựng bảng độ nhạy B1–B4 trong `src/lab13.py` và `report/team/bang_chi_phi.md`, đối chiếu từng số với hướng dẫn chi tiết.
- CP3 · Nhiệm vụ C: Người gắn nhãn 2, gắn độc lập 20 ca lỗi theo năm loại Google PAIR (không trao đổi với Người gắn nhãn 1), rồi so nhãn với Nguyễn Khắc Bào.

### Đóng góp cụ thể

- Viết `KICH_BAN_B1` (9 kịch bản, mỗi dòng chỉ đổi một yếu tố) và các hàm `in_b1_do_nhay`, `in_b2_cap`, `in_b3_gioi_han`, `in_b4_xem_lai_tat_ca` trong `src/lab13.py`; mỗi kịch bản là một lần gọi lại `mo_hinh` của CP1.
- B1: 4.723/4.346 đ (giá token), 6.292/3.562 đ (xem lại), 6.787/3.315 đ (làm lại), 5.506 đ (lương +25%), 4.237/4.111 đ (giới hạn 2/1 lần); tự kiểm tra "giảm một nửa = −½ gấp đôi" đạt.
- B2: 6.543 đ (+46,3%) đúng bằng tổng hai tác động riêng (+5,6% + 40,7%); xếp hạng 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên.
- B3: chi phí cả hệ thống 6.901.220 đ ở giới hạn 2 lần (rẻ nhất cho công ty), không trùng với giới hạn cho CPS thấp nhất (1 lần, 4.111 đ), vì đẩy thêm 85 việc sang nhân viên.
- B4: xem lại 100% `noi_dia` + `hang_nang` cho 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca) [simulated]; mức hoà vốn ≤ 5,1 phút cho mỗi lần xem lại. Mọi dòng từ cột `_simulated` đều có nhãn `simulated`.
- CP3: gắn độc lập 20 ca theo nguyên nhân gốc; so với bộ của Người gắn nhãn 1 đạt đồng thuận 20/20 (100%), phân bổ 4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn hệ thống · 3 Ngầm.

### Bằng chứng

- Commit `c1d9d15` — "feat(CP2): bảng độ nhạy B1-B4" (2026-11-25 15:17:48).
- Commit `3141cd7` — "docs(CP3): gắn nhãn độc lập người 2 cho 20 ca lỗi" (2026-11-25 16:22:17).
- Commit `bfc91d6` — "docs: báo cáo cá nhân Vũ Văn Trường (CP2)" (2026-11-25 15:57:33).
- Commit `10aba67` — "docs(TEAM): bổ sung đóng góp cụ thể của Vũ Văn Trường (CP2, CP3)" (2026-11-25 23:44:19).
- `src/lab13.py`, `report/team/bang_chi_phi.md` (mục B1–B4), `report/team/bang_loi.md`.
- Báo cáo cá nhân: `report/team/2A202603910_VuVanTruong.md`.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
