#def my_function(**students) :
    #print("สวัสดีคุณ" + students["fname"] + " " + students["lname"])
    
#my_function(fname = "Rachchanon", lname = "Seehawong")
def info(**detail) :
    print("ชื่อ" , detail["fname"])
    print("นามสกุล" , detail["lname"])
    print("ชื่อเล่น" , detail["nickname"])
    print("เบอร์โทร" , detail["phone"])
    print("วันเดือนปีเกิด" , detail["date"])

info (fname = "Rachchanon", lname = "Seehawong", nickname = "เนม", phone = "092-407-9036", date = "3 เมษายน 2553")