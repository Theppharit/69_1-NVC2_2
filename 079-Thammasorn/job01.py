proname = input("please input product name: ")
price = float(input("please input product price: "))
vat = float(input("please input VAT rate: "))

output1 = price * vat /100

vatprice = price + output1

print(f"Product: {proname} Product Orignal Price: {price} Added Price VAT: {vatprice}")
