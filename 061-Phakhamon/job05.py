def info (**detail) :
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("เบอร์โทร", detail["phone"])
    print("วันเดือนปีเกิด", detail["date"])
    
info (fname = "ไมเคิล",lname = "สมพร",nickname = "สุข", phone = "0800088800" , date = "23 พฤศจิกายน 2569")