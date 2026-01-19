def tip_calculator():
    bill = float(input("Enter the total bill amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip_amount = bill * (tip_percentage / 100)
    print("The Total Bill is : " + str(bill + tip_amount) + "$")
    
tip_calculator()