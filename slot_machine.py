# Project 11 : Slot machine 

import random

current_balance = 100


def spin_row():
    symbols = ['🍒', '🍉', '🥭', '🔔', '⭐']
    results = [random.choice(symbols) for _ in range(3)]
    return results


def calculate_winnings(results, bet):
    # Example: 3 same symbols → 5x bet, 2 same symbols → 2x bet
    if results.count(results[0]) == 3:
        return bet * 5
    elif len(set(results)) == 2:  # Means 2 symbols are the same
        return bet * 2
    return 0  # No match → no winnings


def main():
    global current_balance
    while True:
        print("\n************************************")
        print("Welcome to the slot machine program!")
        print("Symbols : 🍒 🍉 🥭 🔔 ⭐")
        print("************************************")
        print(f"Current balance: ₹{current_balance}")

        bet_amount_str = input("Enter bet amount (0 to quit): ")

        if not bet_amount_str.isdigit():
            print("❌ Please enter a valid number.")
            continue

        bet_amount = int(bet_amount_str)

        if bet_amount == 0:
            print("Thanks for playing! Final balance:", current_balance)
            break

        if bet_amount > current_balance:
            print("❌ Insufficient balance.")
            continue

        if bet_amount < 0:
            print("❌ Amount must be positive.")
            continue

        current_balance -= bet_amount

        # Spin the slot
        results = spin_row()
        print("🎰 Spin results:", " | ".join(results))

        winnings = calculate_winnings(results, bet_amount)
        if winnings > 0:
            print(f"🎉 You win ₹{winnings}!")
            current_balance += winnings
        else:
            print("😢 No win this time.")

        if current_balance <= 0:
            print("💀 You're out of money. Game over!")
            break


if __name__ == '__main__':
    main()
