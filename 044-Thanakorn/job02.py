def Products(name, priece) :
    priece = (int(input("ใส่ราคาสินค้า:")))
    tax = (int(input("ใส่อัตราภาษี:")))
    print("ภาษี:" + str(priece * tax / 100))
    purchase_price = priece + (priece * tax / 100)
    print("ราคาสุทธิรวมภาษี:" + str(purchase_price))

Products("ขนม1",70)
Products("ขนม2",55)
Products("ขนม3",65)
Products("ขนม4",90)
Products("ขนม5",100)