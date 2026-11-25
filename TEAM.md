# Team

## Thông tin nhóm

- Tên nhóm: Nhom001
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom001-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/workcaominh-gif/K5-L3B-DAY13-Nhom001-LaunchEconomics · nhánh `main` · commit chốt điền trước khi nộp

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Cao Duy Minh | | | `workcaominh-gif` | Người viết code (CP1) |
|   2 | Hoàng Nhật Minh | 2A202603992 | | | Người viết code sau giải lao (CP4) |
|   3 | | | | | Người gắn nhãn 1 |
|   4 | | | | | Người gắn nhãn 2, kiêm giữ hồ sơ |

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

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
