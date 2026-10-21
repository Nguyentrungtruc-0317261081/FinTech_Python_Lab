# 1. Khởi tạo dữ liệu ban đầu
V_goc = 20.0  # Đơn vị: Tỷ VNĐ
ds_delta_ex = [-0.03, 0.00, 0.03]  # Tỷ giá: -3%, 0%, +3%
ds_delta_ir = [-0.02, -0.01, 0.01, 0.02]  # Lãi suất: -2%, -1%, +1%, +2%

print("=== MA TRẬN MÔ PHỎNG RỦI RO DANH MỤC (STRESS TESTING MATRIX) ===")
print(f"Giá trị danh mục gốc (V_goc): {V_goc:.1f} Tỷ VNĐ\n")

# 2. In tiêu đề các cột (Cột đại diện cho Mức thay đổi Lãi suất ΔIr)
header = f"{'ΔEx \\ ΔIr':<12} |"
for delta_ir in ds_delta_ir:
    header += f" {delta_ir*100:+5.1f}%     |"
print(header)
print("-" * len(header))

# 3. Vòng lặp lồng nhau (Nested Loops) để tạo ma trận
# Vòng lặp ngoài: Duyệt qua từng kịch bản Tỷ giá (ΔEx)
for delta_ex in ds_delta_ex:
    row_str = f"ΔEx = {delta_ex*100:+4.1f}%  |"

    # Vòng lặp trong: Duyệt qua từng kịch bản Lãi suất (ΔIr)
    for delta_ir in ds_delta_ir:
        # Tính toán giá trị danh mục mới theo công thức
        V_moi = V_goc * (1 + 1.5 * delta_ex - 2.0 * delta_ir)
        row_str += f" {V_moi:>7.2f} Tỷ |"

    print(row_str)

print("-" * len(header))
