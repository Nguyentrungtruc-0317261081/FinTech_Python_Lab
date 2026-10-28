def convert_currency(amount, from_currency, to_currency="VND"):
    # Chuyển đổi mã tiền tệ về dạng chữ hoa để tránh lỗi nhập thường/hoa
    currency = from_currency.upper()
    
    # Kiểm tra loại tiền tệ và tính toán
    if currency == "USD":
        return amount * 25000
    elif currency == "EUR":
        return amount * 27000
    elif currency == "JPY":
        return amount * 160
    else:
        # Trường hợp loại tiền không được hỗ trợ
        return -1


# ==========================================
# CHƯƠNG TRÌNH KIỂM THỬ (TEST CASES)
# ==========================================

# Test case 1: Chuyển 100 USD
result1 = convert_currency(100, "USD")
print(f"Chuyển 100 USD -> Kết quả: {result1:,}")

# Test case 2: Chuyển 500 EUR
result2 = convert_currency(500, "EUR")
print(f"Chuyển 500 EUR -> Kết quả: {result2:,}")

# Test case 3: Chuyển 1000 AUD (Không hỗ trợ)
result3 = convert_currency(1000, "AUD")
if result3 == -1:
    print(f"Chuyển 1000 AUD -> Kết quả: {result3} (Lỗi: Mã tiền tệ không được hỗ trợ!)")
else:
    print(f"Chuyển 1000 AUD -> Kết quả: {result3:,}")
