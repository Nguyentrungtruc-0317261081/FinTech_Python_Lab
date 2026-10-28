# =========================================================================
# BÀI 1: TÍNH SẢN LƯỢNG HÒA VỐN (BREAK-EVEN POINT - BEP)
# Đặt tên file: 2011xxx_TL6_Bai1.py
# =========================================================================

def calculate_bep(fixed_costs: float, price_per_unit: float, variable_cost_per_unit: float) -> float:
    """
    Tính Sản lượng Hòa vốn (Break-even Point) của doanh nghiệp.
    Công thức:
        BEP = Định phí / (Giá bán đơn vị - Biến phí đơn vị)
   
    Tham số:
        fixed_costs (float): Tổng định phí (VNĐ).
        price_per_unit (float): Giá bán của 1 đơn vị sản phẩm (VNĐ).
        variable_cost_per_unit (float): Biến phí tính cho 1 đơn vị sản phẩm (VNĐ).
       
    Trả về:
        float: Số lượng sản phẩm cần bán để hòa vốn.
    """
    if fixed_costs < 0 or price_per_unit < 0 or variable_cost_per_unit < 0:
        raise ValueError("Các tham số đầu vào không được nhỏ hơn 0.")
   
    contribution_margin = price_per_unit - variable_cost_per_unit
   
    if contribution_margin <= 0:
        raise ValueError("Giá bán đơn vị phải lớn hơn biến phí đơn vị (lãi gộp đơn vị phải > 0).")
   
    bep = fixed_costs / contribution_margin
    return bep


# =========================================================================
# CHƯƠNG TRÌNH KIỂM THỬ (TEST CASE THEO YÊU CẦU)
# =========================================================================
print("=== THỰC HÀNH BÀI 1: TÍNH SẢN LƯỢNG HÒA VỐN (BEP) ===")

# Test case từ đề bài:
# - Định phí = 50,000,000
# - Giá bán = 250,000
# - Biến phí = 150,000
fixed_costs = 50000000.0
price_per_unit = 250000.0
variable_cost_per_unit = 150000.0

break_even_units = calculate_bep(
    fixed_costs=fixed_costs,
    price_per_unit=price_per_unit,
    variable_cost_per_unit=variable_cost_per_unit
)

print(f"Định phí                : {fixed_costs:,.0f} VNĐ")
print(f"Giá bán đơn vị          : {price_per_unit:,.0f} VNĐ")
print(f"Biến phí đơn vị         : {variable_cost_per_unit:,.0f} VNĐ")
print(f"-> Sản lượng hòa vốn    : {break_even_units:,.0f} sản phẩm")

