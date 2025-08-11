# Project : 4 Banking Program

total_balance = 50000  # Shared global balance

def show_balance():
    print(f"Total Balance: ₹{total_balance:,}")

def deposit_money():
    global total_balance
    try:
        deposit_amount = int(input("Enter the amount to deposit: "))
        if deposit_amount > 0:
            total_balance += deposit_amount
            print(f"₹{deposit_amount:,} credited to your account.")
            print(f"Total Balance: ₹{total_balance:,}")
        else:
            print("Negative amount can't be deposited.")
    except ValueError:
        print("Please enter a valid number.")

def withdraw_money():
    global total_balance
    try:
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if withdraw_amount > 0 and total_balance >= withdraw_amount:
            total_balance -= withdraw_amount
            print(f"₹{withdraw_amount:,} debited from your account.")
            print(f"Total Balance: ₹{total_balance:,}")
        elif withdraw_amount > total_balance:
            print("Insufficient balance.")
        else:
            print("Negative amount can't be withdrawn.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
is_running = True

while is_running:
    print("\n*******************")
    print("Welcome to Banking Program!")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Select any choice: "))
        if choice == 1:
            show_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            print("Thank You for using the Banking Program!")
            is_running = False
        else:
            print("Enter a valid choice (1-4).")
    except ValueError:
        print("Please enter a number.")
