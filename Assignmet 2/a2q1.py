def seeds():
    name = str(input("Enter your name: "))
    print("Please select a bundle from the options below: \n\t1: [Beginner] A beginners bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Hobbiest] A hobbiest bundle (15.00$)")
    bundles = {1: ("Beginner", 5), 2: ("Chef", 10), 3: ("Hobbiest", 15)}
    choice = int(input(""))
    while choice != 1 and choice != 2 and choice != 3:
        print("Error: Invalid bundle number, please enter 1, 2, or 3")
        print("Please select a bundle from the options below: \n\t1: [Beginner] A beginners bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Hobbiest] A hobbiest bundle (15.00$)")
        choice = int(input(""))
    num = int(input("Enter the quantity of bundles you want: "))
    total = num * bundles[choice][1]
    print (f"Thanks for your buisness {name}! Here is a receipt:\n----------------\n{num}x {bundles[choice][0]} bundle(s) (${bundles[choice][1]:.2f})\nTotal Cost: (${total:.2f})\nThank you for shopping with us!")
seeds()