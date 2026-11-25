"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()

    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def in_bang_a3(runs, reqs):
    """A3: tách mo_hinh theo từng giá trị của cột loai, in bảng so với BASELINE."""
    print('\nA3 · Tách theo loại yêu cầu')
    for loai in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        con = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, con)
        ty_le_tc = kq['thanh_cong'] / len(con)
        so_lan_chay_tb = con['so_lan_chay'].mean()
        print(f"{loai:12s} n={len(con):4d}  tỉ lệ thành công={ty_le_tc:6.1%}  "
              f"lần chạy/yc={so_lan_chay_tb:4.2f}  cps={kq['cps']:9,.0f}  "
              f"so với {BASELINE:,}={kq['cps'] / BASELINE:5.2f}x")


def in_a4_chi_phi_co_dinh(runs, reqs, chi_phi_co_dinh_thang=40_000_000, khoi_luong_thang=45_000):
    """A4: cộng chi phí cố định/tháng vào cps cho phạm vi noi_dia + hang_nang.
    Tỉ lệ thành công chia cho TOÀN mẫu (reqs), không chỉ phạm vi: tỉ lệ này biểu diễn
    phần việc thành công trong phạm vi trên tổng khối lượng hàng tháng (giả định cùng tỉ trọng loai)."""
    print('\nA4 · Chi phí cố định (phạm vi noi_dia + hang_nang)')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq = mo_hinh(runs, pham_vi)
    ty_le_tc = kq['thanh_cong'] / len(reqs)

    for nhan, kl in (('45.000 yêu cầu/tháng', khoi_luong_thang),
                     ('Một nửa khối lượng', khoi_luong_thang / 2)):
        viec_thanh_cong_thang = kl * ty_le_tc
        chi_phi_co_dinh_moi_viec = chi_phi_co_dinh_thang / viec_thanh_cong_thang
        cps_cong_co_dinh = kq['cps'] + chi_phi_co_dinh_moi_viec
        print(f"{nhan:22s} việc tc/tháng={viec_thanh_cong_thang:9,.0f}  "
              f"cố định/việc={chi_phi_co_dinh_moi_viec:7,.0f}  "
              f"cps+cố định={cps_cong_co_dinh:9,.0f}  so với {BASELINE:,}={cps_cong_co_dinh / BASELINE:5.2f}x")


# ---------- Nhiệm vụ D · Cỡ mẫu pilot ----------
P1, MDE, ALPHA, POWER, ICC = 0.70, 0.05, 0.05, 0.80, 0.02


def co_mau(p1, p2, alpha=ALPHA, power=POWER):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ (kiểm định hai phía), z chính xác."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m - 1) × ICC, m = số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def m_toi_thieu(n_can, so_cum, icc=ICC):
    """m nhỏ nhất sao cho so_cum × m / DE(m) ≥ n_can; None nếu vượt giới hạn so_cum / ICC."""
    mau = so_cum - n_can * icc
    if mau <= 0:
        return None
    return math.ceil(n_can * (1 - icc) / mau)


def in_d1_co_mau():
    print('\nD1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    n5 = co_mau(P1, P1 + MDE)
    print(f'a) Chia theo yêu cầu: {n5:,} yêu cầu mỗi nhóm')

    m = 75
    de = he_so_thiet_ke(m)
    n_cum = math.ceil(n5 * de)
    nv = math.ceil(n_cum / m)
    print(f'b) Theo nhân viên, m={m}: DE={de:.2f}, n={n_cum:,} mỗi nhóm → {nv} người/nhóm, '
          f'tổng {2 * nv} > 40 nhân viên: không đủ người')

    for nhan, c in (('c) 20 nhân viên mỗi nhóm', 20), ('d) 6 depot mỗi nhóm', 6)):
        tran = c / ICC
        print(f'{nhan}: n hiệu dụng tối đa = {c}/{ICC} = {tran:,.0f} '
              f'{"<" if tran < n5 else "≥"} {n5:,} → {"không đạt" if tran < n5 else "đạt"}')

    n6 = co_mau(P1, P1 + 0.06)
    m6 = m_toi_thieu(n6, 20)
    print(f'e) Mức chênh 6 điểm: {n6:,} mỗi nhóm; 20 nhân viên cần m ≥ {m6} yêu cầu/người '
          f'(DE={he_so_thiet_ke(m6):.2f}, tổng {20 * m6:,} yêu cầu/nhóm)')

    # Con số bất lợi: thiết kế cho 6 điểm, nếu tác động thật chỉ 5 điểm thì power còn bao nhiêu?
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        es = proportion_effectsize(P1 + MDE, P1)
        pw = NormalIndPower().power(effect_size=es, nobs1=n6, alpha=ALPHA, ratio=1)
        print(f'   Nếu tác động thật chỉ +5 điểm với n={n6}/nhóm: power ≈ {pw:.2f}')
    except ImportError:
        print('   (cài statsmodels để tính power khi tác động thật chỉ +5 điểm)')


def in_d3_ti_le_mo_lai(reqs):
    print('\nD3 · Tỉ lệ hiện tại để đặt luật dừng')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    for nhan, d in (('Toàn mẫu', reqs), ('noi_dia + hang_nang', pv)):
        mo_lai = d['mo_lai_trong_7_ngay'].astype(int)
        chinh = ((d['dong_trong_24h'].astype(int) == 1) & (mo_lai == 0)).mean()
        print(f'{nhan:20s} mở lại 7 ngày={mo_lai.mean():6.2%} ({mo_lai.sum()}/{len(d)})  '
              f'chỉ số chính (đóng 24h, không mở lại)={chinh:6.2%}')
    so_staff = reqs.groupby('staff_id').size()
    print(f'Nhân viên trong mẫu: {so_staff.size}, yêu cầu/người trong 2 tuần: '
          f'trung bình {so_staff.mean():.1f}, trung vị {so_staff.median():.0f}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\nA2 · Mô hình chi phí từ trace')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    print(f"{'cps/baseline':12s} {ket_qua['cps'] / BASELINE:>14.2f}x")

    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    in_bang_a3(runs, reqs)

    # TODO CP1 · Nhiệm vụ A4: cộng chi phí cố định/tháng (phạm vi noi_dia + hang_nang).
    in_a4_chi_phi_co_dinh(runs, reqs)

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    in_d1_co_mau()
    in_d3_ti_le_mo_lai(reqs)
