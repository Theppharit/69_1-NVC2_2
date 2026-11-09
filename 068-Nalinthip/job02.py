def calculate_vat(price, vat_rate):
    vat + price * vat_rate / 100
    total = price + vat
    return vat, total
for i in range(1, 6):
    print(f"\nสินค้า {i}")
    price = float(input("ป้อนราคาสินค้า:"))
    vat_rate = float(input("ป้อนอัตราภาษี VAT (%): "))
    vat, total = calculate_vat(price , vat_rate)
    
    print(f"ภาษี VAT = {vat:.2f} บาท")
    print(f"ราคาสุทธิ = {total:.2f}บาท")