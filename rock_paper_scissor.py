# Project 3: Rock Paper Scissors Game

import random

choices = ["rock", "paper", "scissors"]
mapping = {"r": "rock", "p": "paper", "s": "scissors"}

def get_user_choice():
    user_input = input("Rock, Paper, Scissors (r/p/s): ").lower()
    if user_input not in mapping:
        print("Enter a valid choice (r/p/s).")
        return None
    return mapping[user_input]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

def main():
    while True:
        for i in range(1, 4):
            print(f"\nRound {i}:")
            user_choice = None
            while user_choice is None:
                user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            determine_winner(user_choice, computer_choice)
        
        exit_choice = input("\nDo you want to continue? (y/n): ").lower()
        if exit_choice == "n":
            print("Thank you for playing!")
            break
        elif exit_choice != "y":
            print("Invalid input. Exiting game.")
            break

if __name__ == "__main__":
    main()
