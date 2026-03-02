def sum_of_multiples():
    sum_of_multiples = 0
    for number in range(1, 50):
        if number % 4 == 0:
            sum_of_multiples += number
    print("Sum:", sum_of_multiples)
sum_of_multiples()