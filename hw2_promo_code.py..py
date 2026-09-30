# hw2_promo_code.py

# 1. Nhập vào Họ Tên đầy đủ
full_name = input("Nhập họ và tên đầy đủ: ")

# 2. Nhập vào Năm sinh
birth_year = input("Nhập năm sinh: ")

# Tách chuỗi họ tên để lấy Tên (phần tử cuối cùng)
name_parts = full_name.strip().split()
first_name = name_parts[-1]  # Lấy tên chính (ví dụ: "Mẹo")

# 3. Tạo mã ưu đãi theo quy tắc:
# Cắt 3 chữ cái đầu của Tên và chuyển thành chữ in hoa [0:3]
name_code = first_name[:3].upper()

# Ghép theo định dạng: [3 chữ cái đầu Tên]-[Năm sinh]-[VIP]
promo_code = f"{name_code}-{birth_year}-VIP"

# In kết quả ra màn hình
print(f"Mã ưu đãi của bạn là: {promo_code}")
