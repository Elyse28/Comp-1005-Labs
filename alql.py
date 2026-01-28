def GuessingGame():
    import random
    max = float(input("Enter the maximum number: "))
    number=random.randint(1,max)
    guess = float(input("Enter your guess: "))
    for i in range(5):
        if guess == number:
            print("You win")
            quit()
        if (number - guess) < (-0.25 * max):
            print("WAY too low!")
        elif (number - guess) > (0.25 * max):
            print("WAY too high!")
        elif (number - guess) > 0:
            print("Too low!")
        else:
            print("Too high!")
        guess = float(input("Enter your guess: "))
        
GuessingGame()