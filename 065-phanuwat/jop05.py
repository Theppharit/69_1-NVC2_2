def info (**detail):
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("อายุ", detail["age"])
    print("น้ำหนัก", detail["weight"])
    
info(fname = "ภานุวัฒน์", lname = "มัดยาดำ", nickname = "เบียร์", age = 20, weight = 58)