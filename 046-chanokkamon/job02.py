
def calcilate_vat(price, vat_rate):
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    return vat_amount, total_price

def main ():
    print("---โปรแกรมคำนวนภาษี  VAT และราคาสุทธิ (จำนวน5ชิ้น)---")
    
    
    vat_rate = float(input("ป้อนอัตราภาษี VAT (%  เช่น 7): "))


    for i in range(1, 6):
        print(f"\n[ชิ้นที่{i}]")
        price = float(input("ป้อนราคาสินค้า: "))

        vat_amount, total_price = calcilate_vat(price, vat_rate)

        print(f" - ภาษี VAT: {vat_amount:.2f} บาท")  
        print(f" - ราคาสุทธิ (รวม VAT):{total_price:.2f}บาท")

if __name__ == "__main__":
   main()    

