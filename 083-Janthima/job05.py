def info (**detail) :
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("อายุ", detail["old"])
    print("สีที่ชอบ", detail["color"])
    
info (fname = "จันทร์ทิมา",lname = "สร้างนอก",nickname = "มะปราง", old = "17" , color = "สีเขียว")