from random import randint
from art import logo
# Constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to set difficulty
def set_difficulty():
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == "easy":
        return EASY_LEVEL_TURNS
    elif game_level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input. Defaulting to 'easy' mode.")
        return EASY_LEVEL_TURNS


# Function to check user's guess
def check_answer(user_guess, actual_number, attempts):
    """Returns the remaining attempts after checking the guess."""
    if user_guess > actual_number:
        print("Too high!")
        return attempts - 1
    elif user_guess < actual_number:
        print("Too low!")
        return attempts - 1
    else:
        print(f"You got it! The correct number was {actual_number}.")
        return 0  # Game ends when the guess is correct


# Main game function
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = randint(1, 100)

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, random_number, attempts)

        if attempts == 0 and guess != random_number:
            print("You've run out of guesses. You lose!")
            return
        elif guess == random_number:
            return
        else:
            print("Guess again.")

game()