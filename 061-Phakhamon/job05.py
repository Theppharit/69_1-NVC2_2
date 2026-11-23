def info (**detail) :
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("งานอดิเรก", detail["hobby"])
    print("สิ่งที่ชอบ", detail["favorite"])
    
info (fname = "ภคมน",lname = "ยังจรูญ",nickname = "เฟรชชี่", hobby = "นอนหลับ" , favorite= "แมว/ของกิน")