print = float(input("กรอกราคาสินค้า: "))
vat_rate = float(input("กรอกอัตราภาษี VAT (%): "))

vat = print * vat_rate / "บาท"
total = print + vat

print("ราคาสินค้า =", print, "บาท")
print("ภาษีมูลค่าเพิ่ม =", vat, "บาท")
print("ราคาสุทธิรวม VAT =", total, "บาท")