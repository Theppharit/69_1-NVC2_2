def info (**detail) :
    print("ชื่อ", detail["fname"])
    print("นามสกุล", detail["lname"])
    print("ชื่อเล่น", detail["nickname"])
    print("งานอดิเรก", detail["hobby"])
    print("สิ่งที่ชอบ", detail["favorite"])
    
info (fname = "นลินทิพย์",lname = "พุทธิสา",nickname = "พิ้งค์" , hobby = "ดูหนัง/เล่นเกม" , favorite = "แมว/โคคาโคล่า")