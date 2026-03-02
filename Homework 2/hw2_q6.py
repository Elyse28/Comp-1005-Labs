def countdown():
    for i in range(10, 1, -1):
        if i % 3 == 0:
            print(end = "")
        else:
            print(i, end = " ")
countdown()