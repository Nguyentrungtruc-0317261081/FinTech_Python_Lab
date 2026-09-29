# Yêu cầu nhập X,Y,N


X = float(input("Nhập tổng hóa đơn (X đồng): "))

Y = float(input("Nhập số tiền tip cho nhân viên (Y%): "))

N = int(input("Nhập số người chia tiền (N tiền): "))


# Tính tổng số tiền sau khi tip
tong_tien_sau_tip = X * (1 + Y / 100)

# Tính tổng số tiền mỗi người phải trả
tien_moi_nguoi = tong_tien_sau_tip / N

# Làm tròn đến số nguyên (0 chữ số thập phân)
tien_can_tra = round(tien_moi_nguoi)


# In kết quả
print(f" Số tiền thực tế mỗi người phải trả là: {tien_can_tra} đồng")
