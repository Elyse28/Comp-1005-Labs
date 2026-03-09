def seeds():
    name = input("Enter your name: ")
    print("Please select a bundle from the options below: \n\t1: [Florist] A Florist bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Gardener] A gardener bundle (15.00$)")
    bundles = {1: ("Florist", 5), 2: ("Chef", 10), 3: ("Gardener", 15)}
    cart = {1: ("Florist", 0), 2: ("Chef", 0), 3: ("Gardener", 0)}
    choice = int(input(""))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Error: Invalid bundle number, please enter 1, 2, 3, or 4")
        print("Please select a bundle from the options below: \n\t1: [Florist] A Florist bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Gardener] A gardener bundle (15.00$)\n\t4: Complete Purchase")
        choice = int(input(""))
    while choice != 4:
        num = int(input(f"Enter the quantity of {bundles[choice][0]} Bundles (${bundles[choice][1]:.2f}) you want: "))
        cart[choice] = (cart[choice][0], cart[choice][1] + num)
        print("Please select a bundle from the options below: \n\t1: [Florist] A Florist bundle (5.00$) \n\t2: [Chef] Chefs Bundle (10.00$) \n\t3: [Gardener] A gardener bundle (15.00$)\n\t4: Complete Purchase")
        choice = int(input(""))
    total = cart[1][1] * bundles[1][1] + cart[2][1] * bundles[2][1] + cart[3][1] * bundles[3][1]
    print(total)
    print (f"Thanks for your buisness {name}! Here is a receipt:\n--------------------------\n{cart[1][1]}x {bundles[1][0]} Bundle (${bundles[1][1]:.2f})\n{cart[2][1]}x {bundles[2][0]} Bundle (${bundles[2][1]:.2f})\n{cart[3][1]}x {bundles[3][0]} Bundle (${bundles[3][1]:.2f})\nTotal Cost: (${total:.2f})\nThank you for shopping with us!")
seeds()