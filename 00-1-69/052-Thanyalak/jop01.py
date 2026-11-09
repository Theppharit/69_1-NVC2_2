price = float(input("ป้อนรหัสสินค้า:  "))
vat_rate = float(input("ป้อนอัตราภาษี vat (%): "))

vat_amount = price * vat_rate / 100
total_price = price + vat_amount

print(f"ภาษี vat: {vat_amount:.2f}บาท")
print(f"ราคาสุทธิรวม vat: {total_price:.2f}บาท")
