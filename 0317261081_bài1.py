# 1. Khởi tạo dữ liệu ban đầu
tuoi = 25
so_du = 0.0
tien_gui = 60000000.0  # 60 triệu VNĐ/năm
lai_suat = 0.10  # Lợi nhuận đầu tư 10%/năm
tang_tien_gui = 0.08  # Tăng trưởng khoản gửi 8%/năm
muc_tieu = 10000000000.0  # 10 tỷ VNĐ

nam = 0

print("=== BÁO CÁO MÔ PHỎNG KẾ HOẠCH TÍCH LŨY HƯU TRÍ ===")
print(f"Mục tiêu: {muc_tieu:,.0f} VNĐ\n")
print("-" * 80)
print(
    f"{'Năm':<5} | {'Tuổi':<6} | {'Số tiền gửi mới (VNĐ)':<22} | {'Tiền lãi (VNĐ)':<18} | {'Tổng tài sản cuối năm (VNĐ)':<25}"
)
print("-" * 80)

# 2. Vòng lặp mô phỏng tích lũy hàng năm
while so_du < muc_tieu:
    nam += 1

    # Tính toán cho năm hiện tại
    tien_lai = so_du * lai_suat
    so_du = so_du + tien_lai + tien_gui

    # In kết quả của năm hiện tại
    print(
        f"{nam:<5} | {tuoi:<6} | {tien_gui:>22,.0f} | {tien_lai:>18,.0f} | {so_du:>25,.0f}"
    )

    # Cập nhật thông số cho năm tiếp theo
    tien_gui *= 1 + tang_tien_gui
    tuoi += 1

print("-" * 80)
print(
    f"\n=> TỔNG KẾT: Người này sẽ đạt mục tiêu 10 tỷ VNĐ ở tuổi {tuoi - 1} (sau {nam} năm tích lũy)."
)
