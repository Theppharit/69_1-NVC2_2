name1 = input("กรอกชื่อสินค้า 1: ")
price1 = int(input("กรอกราคาสินค้า 1: "))
qty1 = int(input("กรอกจำนวนนที่ขาย 1: "))
total1 = price1 * qty1
print("ยอดรวม 1: ", total1)

name2 = input("กรอกชื่อสินค้า 2: ")
price2 = int(input("กรอกราคาสินค้า 2: "))
qty2 = int(input("กรอกจำนวนนที่ขาย 2: "))
total2 = price2 * qty2
print("ยอดรวม 2: ", total2)
Gtotal = total1 + total2
print("ยอดรวมทั้งหมด: ", Gtotal)