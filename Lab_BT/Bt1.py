# Bài tập 1: Mở ví điện tử

ho_ten = input("Nhập họ tên khách hàng: ")
so_dien_thoai = input("Nhập số điện thoại: ")
cccd = input("Nhập số CCCD: ")
so_tien_nap = float(input("Nhập số tiền nạp ban đầu (VND): "))

# Phí mở ví
phi_mo_vi = 50000

# Số dư thực tế sau khi trừ phí
so_du = so_tien_nap - phi_mo_vi

# In kết quả
print("\n===== THÔNG TIN VÍ ĐIỆN TỬ =====")
print("Họ tên:", ho_ten.upper())
print("4 số cuối CCCD:", cccd[-4:])
print("Số tiền nạp:", f"{so_tien_nap:,}")
print("Phí mở ví:", f"{phi_mo_vi:,.0f} VND")
print("Số dư khả dụng:",f"{so_du:,.0f} VND")
