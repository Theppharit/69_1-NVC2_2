#def my_fuction(*numbers):
    #total = 0
    #for number in numbers:
        #total += number
    #return total
#print(my_fuction(1, 2, 3, 4, 5))

def my_function(*numbers) :
    total = 0
    total = (numbers[0]+numbers[1])*numbers[2]
    print(total)

my_function(1, 2, 3)
