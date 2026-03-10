import random
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
    print("Time To Open Bundles!\n--------------------------")
    probabilities = {1: (0.80, 0.15),2: (0.05, 0.50),3: (0.30, 0.40),}
    
    #I used ai a bit for this first for loop
    for bundle_key in (1, 2, 3):
        bundle_name = bundles[bundle_key][0]
        bundle_count = cart[bundle_key][1]
        flower_threshold = probabilities[bundle_key][0]
        herb_threshold = probabilities[bundle_key][0] + probabilities[bundle_key][1]

        for bundle_number in range(1, bundle_count + 1):
            seed_count = random.randint(3, 5)
            print(f"Opening {bundle_name} bundle {bundle_number}")

            for seed_number in range(1, seed_count + 1):
                probability_value = random.random()
                if probability_value <= flower_threshold:
                    seed_type = "Flower"
                elif probability_value <= herb_threshold:
                    seed_type = "Herb"
                else:
                    seed_type = "Vegetable"
                print(f"\tYou recieved a {seed_type} Seed!")
    print("Thank you for shopping with us!")
seeds()