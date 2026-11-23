#def my_function (**student) :
   # print("ควยไรสัส" + student["fname"] + " " + student["lname"])
    #my_function(fname = "chanakan" , lname = "suadmon")
    
def info (**detail) :
    print("ชื่อ" , detail [ "lname"])
    print("นามสกุล" , detail [ "sname"])
    print("ชื่อเล่น" , detail [ "nickname"])
    print("เบอร์โทร" , detail [ "phone"])
    print("วันเดือนปีเกิด" , detail [ "date"])
    
info (fname =  "chanakan" , lname = "ควายป่า" , nickname = "เหี้ย" , phone = 0820688853)