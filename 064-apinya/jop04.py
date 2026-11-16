def myFunction(*num):
    total = num[0]
    for i in num[1:]:
        total = total / i
        print("ผมหาร = ", total)
        
myFunction(100, 2, 5, 2)

    
