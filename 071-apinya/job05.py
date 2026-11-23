def info(**detail):
    print("ชื่อ:", detail["fname"])
    print("นามสกุล:", detail["lname"])
    print("ชื่อเล่น:", detail["nickname"])
    print("เบอร์โทร:", detail["phone"])
    print("วันเดือนปีเกิด:", detail["date"])

    info(fname="Apinya",lname="innok",nickname="Tuta",phone="0651134113",date="11/03/2553")
