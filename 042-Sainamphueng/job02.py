def vat ( price , rate ) :
    tex = price * rate / 100
    return tax , price + tax

for i in range(1, 6):
    price = float