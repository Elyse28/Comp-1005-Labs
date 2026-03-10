def password_check():
    password = input("Enter password: ")
    while password != "comp1005" and password != "comp1405":
        print("Wrong password, try again.")
        password = input("Enter password: ")
    print("Access granted.")
password_check()