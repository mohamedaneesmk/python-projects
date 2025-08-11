# Project 1 : Number Guessing Game

import random

correct_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!!")

try:
    for i in range(3):
        user_guess = int(input(f"Attempt {i+1} - Guess the number between 1 and 100: "))

        if user_guess == correct_number:
            print("Congratulations! You have found the number.")
            print(f"The correct number is {correct_number}")
            break
        elif user_guess > correct_number:
            print("Too High! Guess something lower.")
        else:
            print("Too Low! Guess something higher.")
    else:
        # This runs only if the loop finishes without a break
        print(f"Sorry! You've used all attempts. The correct number was {correct_number}")

except ValueError:
    print("Please enter a valid number.")
