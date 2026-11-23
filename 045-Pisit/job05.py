def info(**detail):
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("ส่วนสูง", detail["height"])
    print("น้ำหนัก", detail["weight"])


info(
    fname="พิสิษฐ์",
    lname="รัตนไพรมณี",
    nickname="เกิ้ล",
    height="169 ซม.",
    weight="85 กก.",
)