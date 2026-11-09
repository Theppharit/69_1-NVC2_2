price = float(input("ป้อนราคาสินค้า: "))
vat_rate = float(input("ป้อนอัตราภาษี VAT (%): "))

vat_amount = price * vat_rate / 100
total_price = price + vat_amount

print(f"ภาษี VAT: {vat_amount:.2f} บาท")
print(f"ราคาสุทธิรวม VAT: {total_price:.2f} บาท")