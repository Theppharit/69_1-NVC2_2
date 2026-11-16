price = float(input("ป้อนราคาสินค้า: "))
vat_rate = float(input("ป้อนอัตราภาษี VAT (%): "))

vat = price * vat_rate / 100
total = price + vat

print("ภาษี VAT =", vat, "บาท")
print("ราคาสุทธิ =", total, "บาท")