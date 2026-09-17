Student1 = { 
    "Name" : "John",
    "Surname" : "Sand",
    "Age" : 16,
    "Phone Number" : "2093652760"
}
Student2 = {
    "Name" : "place holder",
    "Surname" : "place holder",
    "Age" : 16,
    "Phone Number" : "8726340123"
}
Student3 = {
    "Name" : "Ashlsy",
    "Surname" : "Dom",
    "Age" : 17,
    "Phone Number" : "0984032356"
}
Student4 = {
    "Name" : "place holder",
    "Surname" : "place holder",
    "Age" : 16,
    "Phone Number" : "7650980921"
}
Grade11_Room2 = [Student1, Student2, Student3, Student4]

StudentID = int(input("Enter Student ID: "))
if StudentID == 1 :
    print(Grade11_Room2[0])
elif StudentID == 2 :
    print(Grade11_Room2[1])
elif StudentID == 3 :
    print(Grade11_Room2[2])
elif StudentID == 4 :
    print(Grade11_Room2[3])
elif StudentID == 0 :
    print(Grade11_Room2[0])
    print(Grade11_Room2[1])
    print(Grade11_Room2[2])
    print(Grade11_Room2[3])
else :
    print("Incorrect ID or Not on List")
    