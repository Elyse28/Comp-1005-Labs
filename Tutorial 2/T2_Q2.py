def rent_calc():
    rent = float(input("Please input the total rent: "))
    internet = float(input("Please input the internet bill: "))
    Lroom = 15
    Croom = 10
    Mroom = 9
    Vroom = 6
    HouseSize = Vroom + Mroom + Croom + Lroom
    Lprec = Lroom/HouseSize
    Cprec = Croom/HouseSize
    Mprec = Mroom/HouseSize
    Vprec = Vroom/HouseSize
    print("Lindsay will pay " + str(rent*Lprec + internet/4) + "\n Connor will pay " + str(rent*Cprec + internet/4) + "\n Max will pay " + str(rent*Mprec + internet/4) + "\n Vicki will pay " + str(rent*Vprec + internet/4))
    
rent_calc()