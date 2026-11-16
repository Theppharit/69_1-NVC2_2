# def Myfamily(hello ,*members) :
#     for name in members :

#         print(hello, name)
    
# Myfamily("hello","Dad","Mom","Me","Dog")

# def my_fuction(*numbers) :
#     total = 0
#     for num in numbers :
#         total += num
#     return total
    
# print(my_fuction(1,2,3,4,5,6))

def my_funtion(*num) :
    total = 0
    total = (num[0]+num[1])/num[2]
    print(total)
    
my_funtion(2,3,5)