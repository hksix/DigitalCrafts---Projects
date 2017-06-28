#Guess a number
import random
secretN = random.randint(1, 10)
limit = 5
cond = True
tryAgain = False
while cond:
    guess = int(raw_input("guess the number: "))
    if guess == secretN:
        print ('Hooray')
        cond = False
        tryAgain = True
    else:
        if guess > secretN:
            print guess, 'Try again - number is too high'
            limit = limit - 1
            print 'lives left: ', limit
        if guess < secretN:
            print guess, 'Try again - number is too low'
            limit = limit - 1
            print 'lives left:', limit
    if limit <= 0:
        print('GAME OVER')
        cond = False
        tryAgain = True
        while tryAgain:
            again = (raw_input("play again? "))
            if again == "yes":
                tryAgain = False
                cond = True
                limit = 5
            if again == "no":
                print ('Bye')