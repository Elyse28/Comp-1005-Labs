def countdown():
    i = 10
    while i !=1:
        if i % 3 == 0:
            print(end = "")
        else:
            print(i, end = " ")
        i -= 1
countdown()