# 1. Khởi tạo dữ liệu ban đầu
F = 1000000  # Mệnh giá (VNĐ)
c = 0.09  # Lãi suất coupon 9%/năm
N = 10  # Kỳ hạn 10 năm
y = 0.085  # Lợi suất kỳ vọng thị trường (YTM) 8.5%/năm

# 2. Tính số tiền lãi coupon trả hàng năm
C = F * c

print("=== BÁO CÁO ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP ===")
print(f"Mệnh giá (F)             : {F:,.0f} VNĐ")
print(f"Lãi suất coupon (c)      : {c*100:.1f}%/năm")
print(f"Lãi coupon hàng năm (C)  : {C:,.0f} VNĐ")
print(f"Kỳ hạn (N)               : {N} năm")
print(f"Lợi suất kỳ vọng (YTM - y): {y*100:.1f}%/năm\n")

print("-" * 60)
print(f"{'Năm (t)':<10} | {'Dòng tiền (VNĐ)':<20} | {'Giá trị hiện tại PV (VNĐ)':<22}")
print("-" * 60)

# 3. Tính PV của từng khoản lãi coupon qua các năm
tong_pv_coupon = 0.0

for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c
    print(f"Năm {t:<6} | {C:>15,.0f} VNĐ | {pv_c:>18,.0f} VNĐ")

# 4. Tính PV của mệnh giá gốc nhận vào năm cuối (năm N)
pv_f = F / ((1 + y) ** N)

print("-" * 60)
print(f"Tổng PV của các khoản lãi coupon (10 năm) : {tong_pv_coupon:,.0f} VNĐ")
print(f"PV của mệnh giá gốc (nhận vào năm 10)     : {pv_f:,.0f} VNĐ")

# 5. Tính giá lý thuyết của trái phiếu (P0)
gia_trai_phieu = tong_pv_coupon + pv_f
print(f"\n=> GIÁ LÝ THUYẾT CỦA TRÁI PHIẾU (P0)      : {gia_trai_phieu:,.0f} VNĐ")

# 6. Đánh giá trạng thái giá trái phiếu
if gia_trai_phieu > F:
    trang_thai = "Cao hơn mệnh giá (Premium)"
elif gia_trai_phieu < F:
    trang_thai = "Thấp hơn mệnh giá (Discount)"
else:
    trang_thai = "Đúng mệnh giá (Par)"

print(f"=> PHÂN LOẠI TRÁI PHIẾU                      : {trang_thai}")
