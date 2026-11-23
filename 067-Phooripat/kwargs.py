#def my_funtion (**student) :
    #print("สวัสดีคุณ" + student["fname"] + " " + student["laname"])

#my_funtion(fname = "Phooripat", laname = "Jirapattaranan")

def info (**detail) :
    print("ชื่อ" , detail["fname"])
    print("นามสกุล" , detail["laname"] )
    print("ชื่อเล่น" , detail["nickname"])
    print("เบอร์โทร" , detail["phone"])
    print("วันเดือนปีเกิด" , detail["date"])

info (fname = "Phooripat", laname = "Jirapattaranan", nickname = "Few", phone = "0623162070", date = "12 กันยายน 2549")