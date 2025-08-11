# Project 2: Dice Rolling Game in Python 

import random

def roll_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(f"You rolled: ({num1}, {num2})")

def main():
    print("🎲 Welcome to the Dice Rolling Game!")
    while True:
        choice = input("Roll the dice? (y/n): ").strip().lower()
        if choice == 'y':
            roll_dice()
        elif choice == 'n':
            print("Thanks for playing! 👋")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
