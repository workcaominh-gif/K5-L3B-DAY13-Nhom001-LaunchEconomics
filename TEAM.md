# Team

## Thông tin nhóm

- Tên nhóm: Nhom001
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom001-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/workcaominh-gif/K5-L3B-DAY13-Nhom001-LaunchEconomics · nhánh `main` · commit chốt = HEAD của `main` lúc nộp (`git log -1 --format=%h`)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Cao Duy Minh | 2A202603988 | | `workcaominh-gif` | Người viết code (CP1) |
|   2 | Hoàng Nhật Minh | 2A202603992 | | | Người viết code sau giải lao (CP4) |
|   3 | Nguyễn Khắc Bào | 2A202604072 | baonk.invzble.z@gmail.com | `invzble zone` | Người gắn nhãn 1 (CP3) |
|   4 | Vũ Văn Trường | 2A202603910 | tini.vu.0@gmail.com | `Sz3RO` | Người kiểm số (CP2), Người gắn nhãn 2 (CP3) |
|   5 | Hoàng Thế Duyệt | 2A202603980 | | `theduythg` | Người giữ hồ sơ & tổng hợp CP5 (Nhiệm vụ E) |

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
- `src/lab13.py`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `report/team/phieu_cham.md`.
- Báo cáo cá nhân: `report/team/2A202603980_HoangTheDuyet.md`.

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
