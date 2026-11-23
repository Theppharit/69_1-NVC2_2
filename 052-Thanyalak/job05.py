def info(**detail)  :
    print("ชื่อ",detail["fname"])
    print("นามสกุล",detail["lname"])
    print("ชื่อเล่น",detail["nickname"])
    print("สีที่ชอบ",detail["color"])
    print("สัตว์ที่ชอบ",detail["animal"])
    
info(fname = "Thanyalak", lname = "Phuraya", nickname = "noon", color = "Sky Blue",animal = "cat")