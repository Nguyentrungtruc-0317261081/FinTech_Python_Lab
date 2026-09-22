# Bài tập 2: Tính hóa đơn bán lẻ

ten_san_pham = input("Nhập tên sản phẩm: ")
so_luong = int(input("Nhập số lượng: "))
don_gia = float(input("Nhập đơn giá: "))

# Tính tổng tiền hàng
tong_tien_hang = so_luong * don_gia

# Tính thuế VAT 8%
thue_vat = tong_tien_hang * 0.08

# Tính tổng thanh toán
tong_thanh_toan = tong_tien_hang + thue_vat

# In hóa đơn
print("\n===== HÓA ĐƠN BÁN HÀNG =====")
print("Tên sản phẩm:", ten_san_pham)
print("Số lượng:", so_luong)
print("Đơn giá:",f"{don_gia:,.0f}")
print("Tổng tiền hàng",f"{tong_tien_hang:,.0f}")
print("Thuê VAT (8%):", f"{thue_vat:,.0f}")
print("Tổng thanh toán:", f"{tong_thanh_toan:,.0f}")



