# Khởi tạo dữ liệu
cash_flows = [100000000, 120000000, 150000000, 180000000, 200000000]
r = 0.10 # Tỷ lệ chiết khấu 10%
npv = 0.0 # Biến cộng dồn


print("===BẢNG TÍNH DÒNG TIỀN CHIẾU KHẤU (DCF)")
print(f"{'Năm':<5} | {'Dòng tiền (CF)':<20}| {'Giá trị hiện tại (PV)':<20}")
print("-" * 52)


# Duyệt qua từng năm để tính toán
for i in range(len(cash_flows)):
    nam = i + 1 # Chỉ số index bắt đầu từ 0, nên cần cộng 1 để ra số năm
    cf = cash_flows[i]

    # Tính PV
    pv = cf / ((1 + r) ** nam)
    npv += pv # Cộng dồn vào NPV tổng


    print(f"{nam:<5} | {cf:>15,.0f} VNĐ | {pv:>15,.0f} VNĐ")

    
print("-" * 52)
print(f"TỔNG GIÁ TRỊ DỰ ÁN (NPV): {npv:,.0f} VNĐ")
    
