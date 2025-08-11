import random

def get_user_choice():
    user_input = input("Rock, Paper or Scissor? (r/p/s): ").strip().lower()
    mapping = {'r': 'rock', 'p': 'paper', 's': 'scissor'}
    return mapping.get(user_input)

def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])

def determine_winner(user, computer):
    print(f"\nYou played: {user}")
    print(f"Computer played: {computer}")
    
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

def main():
    print("🎮 Welcome to Rock, Paper, Scissors!")

    for i in range(1, 4):
        print(f"\n🔁 Round {i}")
        user_choice = get_user_choice()
        if user_choice:
            computer_choice = get_computer_choice()
            determine_winner(user_choice, computer_choice)
        else:
            print("❌ Invalid input. Please enter r, p, or s.")

    exit_choice = input("\nDo you want to play again? (y/n): ").strip().lower()
    if exit_choice == 'y':
        main()  # restart the game
    else:
        print("👋 Thank you for playing!")

if __name__ == "__main__":
    main()
