__name__ = "Milk"
Milkb = input("กรอกราคานม:")
MilkN = input("กรอกจำนวนสินค้า:")
print("ชื่อสินค้า: "+__name__)
print("ราคาต่อชิ้น: "+Milkb)
print("จำนวนที่ขาย: "+MilkN)

__name__ = "Cereal"
Cerealb = input("กรอกราคาซีเลี้ยว:")
CerealN = input("กรอกจำนวนสินค้า:")
print("ชื่อสินค้า: "+__name__)
print("ราคาต่อชิ้น: "+Cerealb)
print("จำนวนที่ขาย: "+CerealN)
print("สินค้าทั้งหมด2รายการ")
print("ยอดรวมสินค้า")
print(int(Milkb)*int(MilkN))
print(int(Cerealb)*int(CerealN))