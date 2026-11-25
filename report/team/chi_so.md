# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Ba dòng đầu do `src/lab13.py` (`in_e1_chi_so`) tính trực tiếp từ `logix_requests.csv`.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng | Tự đề xuất: tỉ lệ **giữ** gợi ý của nhân viên | `quyet_dinh_xem_lai` bằng `giu`, chia số yêu cầu được xem lại (`giu` + `sua` + `bo`) | Không cần tính |
| An toàn | Tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn có `so_tien_da_hoan ≠ so_tien_dung` trong mẫu kiểm tra, chia số đơn được kiểm tra | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", **không** viết "trợ lý đã nâng chỉ số từ 0,70": đợt chạy thử không có nhóm đối chứng. Baseline 0,70 trong `pilot_plan.yaml` là con số đề bài cho, không phải kết quả đo được của nhóm.

## Danh sách event

Mười event (tối thiểu sáu), mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra trên màn hình |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (giu/sua/bo), `phut_xem_lai` (đo thật), `trace_id` | Khi bấm gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Hằng tuần, theo lịch kiểm tra mẫu |

**Kiểm tra chéo** — với mỗi chỉ số ở bảng E1, event dùng để tính:

- **Chính (82,83%)**: `refund_request_created` cho mẫu số (1.200), `ticket_closed` cho `dong_trong_24h`, `ticket_reopened` cho `mo_lai_trong_7_ngay`. Tính được.
- **Dùng (27,12%)**: `agent_suggestion_shown` đếm số yêu cầu được xem lại (177), `staff_review_decision` cho `sua`/`bo` (48). Tính được.
- **An toàn (4,25%)**: `ticket_reopened` (51) chia `refund_request_created` (1.200). Tính được.
- **Dùng tự đề xuất (tỉ lệ giữ gợi ý)**: `staff_review_decision`, lấy `giu` chia tổng `giu` + `sua` + `bo`. Tính được.
- **An toàn tự đề xuất (sai tiền qua kiểm tra mẫu)**: `audit_sample_checked`, so `so_tien_da_hoan` với `so_tien_dung`. Tính được — đây là event duy nhất bắt được lỗi ngầm (ca 5, 17) mà `ticket_reopened` không thấy.

Không có chỉ số nào trong bảng E1 rơi vào trạng thái "chưa đo được". Lưu ý `phut_xem_lai` và `phut_lam_lai` trong hai cột `_simulated` của dữ liệu lab là giả lập; khi triển khai pilot phải đọc giá trị thật từ `staff_review_decision` và `staff_rework_completed`.

## E2 · Rủi ro kinh tế

Số lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`, CP2). Mọi số là `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, cps lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi `noi_dia` + `hang_nang`) | Thu hẹp về `noi_dia`, rà 20 trace làm lại có `staff_rework_completed` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] | Tỉ lệ yêu cầu được xem lại còn > 50% cuối bước rollout 0,25 | Giảm xem lại theo bậc khi tỉ lệ `sua` + `bo` < 15%; mỗi lần xem lại ≤ 5,1 phút | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
