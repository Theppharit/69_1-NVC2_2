def info(**detail):
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("ส่วนสูง", detail["height"])
    print("น้ำหนัก", detail["weight"])


info(
    fname="eakphisak",
    lname="Thrapursawat",
    nickname="เป้",
    height="175 ซม.",
    weight="55.5 กก.",
)
