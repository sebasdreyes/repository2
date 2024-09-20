import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            guessed = True

number_guessing_game()
