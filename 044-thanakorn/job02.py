def calculate_vat(price, vat_rate):
    vat = price * vat_rate / 100
    net_price = price + vat
    return vat, net_price
for i in range(1, 6):
    print("\nสินค้า", i)

    price = float(input("ป้อนราคาสินค้า: "))
    vat_rate = float(input("ป้อนอัตราภาษี VAT (%): "))

    # เรียกใช้ฟังก์ชัน
    vat, net_price = calculate_vat(price, vat_rate)

    # แสดงผลลัพธ์
    print("ราคาสินค้า:", price, "บาท")
    print("ภาษี VAT:", vat, "บาท")
    print("ราคาสุทธิรวม VAT:", net_price, "บาท")