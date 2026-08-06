name1 = input("กรอกชื่อสินค้ 1: ")
price1 = int(input("กรอกราคาต่อชิ้น 1: "))
qty1 = int(input("กรอกจำนวนที่ขาย 1: "))
total1 = price1 * qty1
print("ยอดรวม 1: ", total1)

name2 = input("กรอกชื่อสินค้า 2: ")
price2 = int(input("กรอกชื่อสินค้า 2: "))
qty2 = int(input("กรอกจำนวนที่ขาย 2: "))
total2 = price2 * qty2
print("ยอดรวม 2: ", total2)
Grandtotal = total1 + total2
print("ยอดรวมทั้งหมด : ", Grandtotal)