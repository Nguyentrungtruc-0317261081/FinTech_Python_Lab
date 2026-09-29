# Yêu cầu người dùng nhập Tổng vốn ban đầu và Tổng giá trị bán ra

tong_von_ban_dau = float(input("Nhập tổng vốn ban đầu (Initial Investment): "))
tong_gia_tri_ban_ra = float(input("Nhập tổng giá trị bán ra (Final Value): "))

# Tính lợi nhuận ròng (Final Value - Initial Investment)
loi_nhuan_rong = tong_gia_tri_ban_ra - tong_von_ban_dau

# Tính tỉ lệ Roi(%)
roi = (loi_nhuan_rong / tong_von_ban_dau) * 100

# In kết quả

print(f"lợi nhuận ròng", loi_nhuan_rong)
print(f"Tỷ lệ Roi (%)", roi)
