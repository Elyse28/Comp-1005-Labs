def timetable():
    number = int(input("Enter a number: "))
    for i in range (10):
        print(f"{number} x {i+1} = {number * (i+1)}")
timetable()