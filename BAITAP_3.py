# 1. Khai báo tham số khoản vay
khoan_vay = 1000000000.0 # 1 tỷ VNĐ
so_thang = 12
lai_suat_nam = 0.12      # 12%/năm

# Tính toán các hằng số
lai_suat_thang = lai_suat_nam / 12
goc_tra_deu = khoan_vay / so_thang
du_no = khoan_vay

print("=== LỊCH TRẢ NỢ VAY MUA NHÀ (PHƯƠNG PHÁP GỐC ĐỀU) ===")
# Tạo Header bảng
header = f"{'Tháng':<5} | {'Dư nợ đầu kỳ':<15} | {'Nợ gốc':<15} |{'Lãi':<15} | {'Tổng trả':<15} | {'Dư nợ cuối kỳ':<15}"
print(header)
print("-" * len(header))


# 2. Vòng lặp tính toán từng tháng
for thang in range(1, so_thang + 1):
    du_no_dau_ky = du_no
    
    # Lãi tính trên dư nợ thực tế
    tien_lai = du_no_dau_ky * lai_suat_thang
    
    # Tổng tiền khách hàng phải trả tháng này
    tong_tra = goc_tra_deu + tien_lai

    # Trừ nợ gốc
    du_no -= goc_tra_deu

    # Khử sai số làm tròn ở tháng cuối cùng
    if du_no < 1:
        du_no = 0

    # 3. In thông tin dòng
print(f"{thang:<5} | {du_no_dau_ky:>11,.0f} VNĐ | {goc_tra_deu:>11,.0f}VNĐ | {tien_lai:>11,.0f} VNĐ | {tong_tra:>11,.0f} VNĐ | {du_no:>11,.0f}VNĐ")
print("-" * len(header))
