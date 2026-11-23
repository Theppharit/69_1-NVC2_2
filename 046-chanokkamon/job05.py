def info (**datail) :
    print("ชื่อ", datail["fname"])
    print("นามสกุล", datail["lname"])
    print("ชื่อเล่น", datail["nickname"])
    print("อายุ", datail["age"])
    print("สัญชาติ ", datail["nationality"])

info (fname = "ชนกกมล" , lname = "โกวิทชาคร" , nickname =
     "นํ้าตาล" , age = 16, nationality = "ไทย")
