def info(**detail):
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("ส่วนสูง", detail["height"])
    print("น้ำหนัก", detail["weight"])


info(
    fname="ธนกร",
    lname="คงเกษม",
    nickname="เป้",
    height="169 ซม.",
    weight="69.5 กก.",
)
