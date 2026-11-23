def info(**detail):
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("ส่วนสูง", detail["height"])
    print("น้ำหนัก", detail["weight"])


info(fname="จิรกานต์", lname="ฮันสูงเนิน", nickname="เพลง", height="155", weight="45 กก.")