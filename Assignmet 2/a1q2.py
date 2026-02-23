def seeds():
    name = str(input("Enter your name: "))
    print("Please select a bundle from the options below: \n\t1: [Beginner] A beginners bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Hobbiest] A hobbiest bundle (15.00$)\n\t4: Complete Purchase")
    bundles = {1: ("Beginner", 5), 2: ("Chef", 10), 3: ("Hobbiest", 15)}
    cart = {1: ("Beginner", 0), 2: ("Chef", 0), 3: ("Hobbiest", 0)}
    choice = int(input(""))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Error: Invalid bundle number, please enter 1, 2, 3, or 4")
        print("Please select a bundle from the options below: \n\t1: [Beginner] A beginners bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Hobbiest] A hobbiest bundle (15.00$)\n\t4: Complete Purchase")
        choice = int(input(""))
    while choice != 4:
        num = int(input(f"Enter the quantity of {bundles[choice][0]} Bundles (${bundles[choice][1]:.2f}) you want: "))
        cart[choice] = (cart[choice][0], cart[choice][1] + num)
        print("Please select a bundle from the options below: \n\t1: [Beginner] A beginners bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Hobbiest] A hobbiest bundle (15.00$)\n\t4: Complete Purchase")
        choice = int(input(""))
    total = cart[1][1] * bundles[1][1] + cart[2][1] * bundles[2][1] + cart[3][1] * bundles[3][1]
    print(total)
    print (f"Thanks for your buisness {name}! Here is a receipt:\n--------------------------\n{cart[1][1]}x Beginner's Bundle (5.00$)\n{cart[2][1]}x Chef's Bundle (10.00$)\n{cart[3][1]}x Hobbiest's Bundle (15.00$)\nTotal Cost: (${total:.2f})\nThank you for shopping with us!")
seeds()