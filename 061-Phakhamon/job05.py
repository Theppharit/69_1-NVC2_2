def info (**detail) :
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("สิ่งที่ชอบ", detail["myfavorite"])
    print("งานอดิเรก", detail["hobby"])
    
info (fname = "ภคมน",lname = "ยังจรูญ",nickname = "เฟรชชี่", myfavorite = "แมว/ของกิน" , hobby = "นอน")