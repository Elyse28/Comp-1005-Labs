def grade_calc():
    percentage_grade = float(input("Enter your final grade percentage: "))
    if percentage_grade >= 90 or percentage_grade <= 100:
        print("Your letter grade is: A+")
    elif percentage_grade >= 85 or percentage_grade <= 89:
        print("Your letter grade is: A")
    elif percentage_grade >= 80 or percentage_grade <= 84:
        print("Your letter grade is: A-")
    elif percentage_grade >= 77 or percentage_grade <= 79:
        print("Your letter grade is: B+")
    elif percentage_grade >= 73 or percentage_grade <= 76:
        print("Your letter grade is: B")
    elif percentage_grade >= 70 or percentage_grade <= 72:
        print("Your letter grade is: B-")
    elif percentage_grade >= 67 or percentage_grade <= 69:
        print("Your letter grade is: C+")
    elif percentage_grade >= 63 or percentage_grade <= 66:
        print("Your letter grade is: C")
    elif percentage_grade >= 60 or percentage_grade <= 62:
        print("Your letter grade is: C-")
    elif percentage_grade >= 57 or percentage_grade <= 59:
        print("Your letter grade is: D+")
    elif percentage_grade >= 53 or percentage_grade <= 56:
        print("Your letter grade is: D")
    elif percentage_grade >= 50 or percentage_grade <= 52:
        print("Your letter grade is: D-")
    elif percentage_grade < 50:
        print("Your letter grade is: F")
    else:
        print("Error: Please enter a valid percentage between 0 and 100.")
        
grade_calc()