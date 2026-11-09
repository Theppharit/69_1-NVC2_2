def Products(name, price):
    print("ชื่อสินค้า:", name)
    print("ราคาสินค้า:", price)
    print("ภาษี VAT:", price * 7 / 100)
    print("ราคาสุทธิ", price + (price * 7 /100))
    print("----------------------")
    
    
Products("ขนม", 40)
Products("น้ำ", 20)
Products("ยางลบ", 10)
Products("หนังสือ", 30)
Products("ดินสอ", 15)