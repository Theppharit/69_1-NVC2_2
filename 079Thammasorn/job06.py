number = int(input("กรุณากรอกแม่สูตรคูณ: "))
multiplier = 1

while multiplier <= 12:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier += 1