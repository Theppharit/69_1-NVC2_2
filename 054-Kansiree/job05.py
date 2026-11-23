def info(**detail)  :
    print("ชื่อ",detail["fname"])
    print("นามสกุล",detail["lname"])
    print("ชื่อเล่น",detail["nickname"])
    print("สีที่ชอบ",detail["color"])
    print("สัตว์ที่ชอบ",detail["animal"])
    
info(fname = "Kansiree", lname = "Junlasana", nickname = "nuknick", color = "Pink",animal = "cat")