# Khởi tạo dữ liệu hệ thống
ma_pin_goc = "123456"
gioi_han = 3
so_lan_thu = 0

print("=== HỆ THỐNG ATM XIN CHÀO ===")

while so_lan_thu < gioi_han:
    pin_nhap = input("Vui lòng nhập mã PIN (6 chữ số): ")
    so_lan_thu += 1  # Tăng số lần đã thử lên 1

    if pin_nhap == ma_pin_goc:
        print(
            "\n[THÀNH CÔNG] Đăng nhập hợp lệ. Mời quý khách thực hiện giao dịch."
        )
        break  # Ngắt vòng lặp ngay khi nhập đúng
    else:
        so_lan_con_lai = gioi_han - so_lan_thu
        print("[LỖI] Mã PIN không chính xác!")
        if so_lan_con_lai > 0:
            print(f"-> Quý khách còn {so_lan_con_lai} lần thử.\n")
        else:
            print("\n(CẢNH BÁO AN NINH) Nhập sai quá 3 lần. Thẻ đã bị khóa!")
