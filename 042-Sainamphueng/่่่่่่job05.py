def info (**detail) :
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("อายุ", detail["old"])
    print("สีที่ชอบ", detail["color"])
    
info (fname = "สายน้ำผึ้ง",lname = "วงษ์งาม",nickname = "ลูกหว้า", old = "16" , color = "สีแดง")