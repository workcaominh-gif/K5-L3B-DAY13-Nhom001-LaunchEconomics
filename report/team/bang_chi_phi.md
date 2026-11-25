# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | | đo từ trace |

- Chi phí mỗi việc thành công gấp 16,3 lần "hoá đơn chia số yêu cầu" (4.472 ÷ 275).
- Khoản lớn nhất là làm lại, 51,8% tổng chi phí [simulated]; tiếp theo xem lại 40,7% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- `quoc_te` không đáng để trợ lý xử lý (1,88× baseline, chỉ 27,3% thành công). Chạy lại tới 3 lần không giúp: tỉ lệ đúng giảm dần theo lần thử (lần 1 ~30%, lần 2 ~11,4%, lần 3 ~2,2%) — lỗi lặp lại trên cùng yêu cầu.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định không đổi kết luận ở quy mô đầy đủ (vẫn rẻ hơn baseline, 0,38×), nhưng tăng mạnh khi khối lượng giảm một nửa (0,48×) — pilot chạy ở quy mô nhỏ hơn cần tính lại.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8% khi gấp đôi) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1% khi tăng 25%)

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ, cả hệ thống = tổng trợ lý + 12.000 đ × yêu cầu không thành công) [simulated]. Không trùng: cps thấp nhất ở giới hạn 1 lần (4.111 đ), nhưng đẩy thêm 85 việc sang nhân viên, làm cả hệ thống đắt hơn 548.561 đ.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 948 yêu cầu × 5 phút xem lại + 48 ca × 9 phút làm lại + 224.513 đ token/tool = 10.568.513 đ ÷ 900 việc thành công = **11.743 đ = 0,98×** [simulated]. Nếu dùng mức làm lại trung bình trong dữ liệu (15,3 phút/ca) thì 12.415 đ = 1,03×, đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại chiếm ~90% chi phí, nên xem lại 100% thì trợ lý gần như không tiết kiệm gì. Pilot phải đo được tỉ lệ xem lại có thể giảm an toàn tới đâu và mỗi lần xem lại có ≤ 5,1 phút (hoà vốn với 9 phút làm lại; ≤ 4,8 phút với 15,3 phút) không.
