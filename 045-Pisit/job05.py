def info(**detail):
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("ส่วนสูง", detail["phone"])
    print("น้ำหนัก", detail["date"])


info(
    fname="พิสิษฐ์",
    lname="รัตนไพรมณี",
    nickname="เกิ้ล",
    phone="169 ซม.",
    date="85 กก.",
)