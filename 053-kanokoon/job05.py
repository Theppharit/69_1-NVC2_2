def info(**detail):
    print("ชื่อ:", detail["fname"])
    print("นามสกุล:", detail["lname"])
    print("ชื่อเล่น:", detail["nickname"])
    print("เบอร์โทร:", detail["phone"])
    print("วันเดือนปีเกิด:", detail["date"])

    info(
    fname="Kanokoon",lname="Phinyophap",nickname="foremost",phone="0821587954",date="09/07/2551")
