def calculate_vat(price, vat_rate):
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    return vat_amount, total_price
for i in range(1, 6):
    print(f"\n--- สินค้าชิ้นที่ {i} ---")
    price = float(input("กรุณากรอกราคาสินค้า (บาท): "))
    vat_rate = float(input("กรุณากรอกอัตราภาษี VAT (%): "))
    vat, total = calculate_vat(price, vat_rate)
    print(f"ภาษี VAT ({vat_rate}%): {vat:,.2f} บาท")
    print(f"ราคาสุทธิ (รวม VAT): {total:,.2f} บาท")
