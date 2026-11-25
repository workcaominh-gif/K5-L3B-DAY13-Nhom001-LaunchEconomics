# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom001 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ toàn mẫu = 0,37× của 12.000 đ; riêng phạm vi `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 40 triệu/tháng thành 4.599 đ = 0,38× [simulated] | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại (+51,8% khi gấp đôi, lên 6.787 đ) · Tỉ lệ xem lại (+40,7%, 6.292 đ) · Lương nhân viên (+23,1% khi tăng 25%, 5.506 đ) [simulated]. Giá token chỉ +5,6% | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | Rẻ hơn ở phạm vi đề xuất: 0,28× (3.414 đ) và 0,38× sau cố định [simulated]. Không đáng dùng cho `quoc_te`: 22.515 đ = 1,88×, tỉ lệ thành công 27,3% — chạy lại tới 3 lần vẫn không cứu được | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · dùng (bỏ qua gợi ý) 27,12% (48/177) · an toàn (mở lại 7 ngày) 4,25% (51/1.200). Chưa có đối chứng nên không nói trợ lý đã nâng chỉ số | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 20/20 (100%), khớp 5 loại Google PAIR (4 người dùng, 5 hệ thống, 4 ngữ cảnh, 4 giới hạn, 3 ngầm); đủ 5 biện pháp khắc phục đo được | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20 (đúng 20 cụm/nhóm, bốc thăm seed 20261207), mde 0,06, 859 việc/nhóm (299 yêu cầu/người), ba luật dừng đủ bốn vế, quyết định 2027-01-05. Đánh đổi: nếu tác động thật chỉ +5 điểm thì power ≈ 0,64 | Giả lập | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2: +51,8% → 6.787 đ [simulated]; xem lại 100%: 11.743 đ = 0,98× (12.415 đ = 1,03× với 15,3 phút/ca) [simulated]; khối lượng giảm một nửa: +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện**

Điều kiện để chuyển từ Gate 2a sang pilot (mỗi điều kiện có người chịu trách nhiệm và ngày kiểm tra):

1. **Phạm vi:** chỉ `noi_dia` + `hang_nang` ở cả 12 depot; loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (điều khoản riêng) khỏi pilot — PM trợ lý hoàn phí, kiểm tra trước ngày bắt đầu 2026-12-07.
2. **Cỡ mẫu và ngưỡng:** chấp nhận mde 0,06 (859 việc/nhóm, 299 yêu cầu/người), ghi rõ power chỉ ≈ 0,64 nếu tác động thật +5 điểm; tuyệt đối không kết luận hiệu quả ở mức +5 điểm — Giám đốc vận hành, kiểm tra tại bước rollout 0,50 (tuần 3).
3. **An toàn và chi phí:** giữ ba luật dừng của `pilot_plan.yaml` (mở lại chênh ≥ 2 điểm hoặc > 6% tuyệt đối, cps > 8.000 đ, bỏ qua gợi ý > 40%); Giám đốc vận hành có quyền tắt trợ lý trong 30 phút — kiểm tra hằng tuần từ 2026-12-07 đến 2027-01-05.
4. **Xem lại:** đo tỉ lệ xem lại và thời gian xem lại thật thay vì cột `_simulated`; mỗi lần xem lại phải ≤ 5,1 phút, nếu không đạt thì dừng mở rộng — Trưởng nhóm CSKH, kiểm tra cuối tuần 1 và bước 0,25.

Con số bất lợi đã được nêu ngay trong hồ sơ: chi phí gần sát baseline nếu phải xem lại 100% (0,98×–1,03×) và pilot không đủ power để thấy mức +5 điểm. Đề xuất Go có điều kiện vì chi phí trong phạm vi hẹp vẫn thấp hơn nhân viên tự làm (0,38×), nhưng chỉ khi bốn điều kiện trên được giữ.
