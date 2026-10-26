ราคาสินค้า = float(input("ป้อนราคาสินค้า: "))
ภาษี = float(input("ป้อนอัตราภาษี VAT (%): "))

ภาษีมูลค่าเพิ่ม = price * vat_rate / 100
total_price = price + vat_amount

print(f"ภาษี VAT: {vat_amount:.2f} บาท")
print(f"ราคาสุทธิรวม VAT: {ราคารวม:.2f} บาท")