price = float(input("ป้อนรายได้:"))
vat = float(input("ป้อนอัตราภาษี: "))
vat1 = price * (vat / 100)
total = price + vat1

print("ภาษี:", vat1)
print("ราคารวม:", total)