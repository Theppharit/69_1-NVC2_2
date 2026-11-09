
def vat(price, rate):
    tax = price * rate / 100
    return tax, price + tax

for i in range(1, 6):
    price = float(input("ราคาสินค้า: "))
    rate = float(input("ภาษี VAT (%): "))

    tax, total = vat(price, rate)
    
    print("VAT =", tax)
    print("ราคาสุทธิ =", total)