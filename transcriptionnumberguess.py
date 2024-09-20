import random

def number_guessing_game():
    numbertoguess = random.randint(1,10)
    attempts=0
    guessed=False

    while not guessed:
            guess = int(input("guess a number 1-10"))
            attempts+=1

            if guess < numbertoguess: print("too low")
            elif guess > numbertoguess: print("too high")
            else: 
                 print("congratulations") 
                 guessed = True

number_guessing_game()
