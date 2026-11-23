def info(**detil):
    print("ชื่อ", detil["fname"])
    print("นามสกุล", detil["lname"])
    print("ชื่อเล่น", detil["nickname"])
    print("เบอร์โทร", detil["phone"])
    print("วันเดือนปีเกิด", detil["date"])

    info(fname="มิ้น", lname="จงแก้ว", nickname="มิ้น",phone="0912345678", date="26มิถุนายน 2551") 