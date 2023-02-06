def guess():
    import random
    guess = int(input("enter your guess in range 1 to 1000: "))
    robo_guess = random.randint(1, 1000)

    if guess == robo_guess:
        print("Your guess is right")
    elif guess > robo_guess:
        print("Your guess is bigger robo guess. Robo guess is " + str(robo_guess))
    elif guess < robo_guess:
        print("Your guess is smaller robo guess. Robo guess is " + str(robo_guess))
    else:
       print("Your guess is away . Robo guess is " + str(robo_guess))
guess()
