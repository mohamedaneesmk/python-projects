# Project 6: Shopping cart program

store = {
    "apple":40,
    "orange":35,
    "banana":20,
    "milk":15,
    "cookies":10
}

cart = []
is_locked = False 

def display_cart():
    if not cart:
        print("No item in the cart")
        return
    else:
        print("Your cart")
        total = 0
        # Cast cart to list to support tuple type too
        temp_cart = list(cart)  
        for item in set(temp_cart):
            quantity = temp_cart.count(item)
            cost = store[item] * quantity
            print(f"{item} x {quantity} = ₹{cost}")
            total += cost
        print(f"Total cost : ₹{total}")

while True:
    print("Welcome to Shopping cart program")
    print("***********************************")
    for items, prices in store.items():
        print(f"{items} = ₹{prices}")
    
    print()
    print("1. Add item")
    print("2. View Cart")
    print("3. Remove duplicates")
    print("4. Lock the cart")
    print("5. Exit")
    
    choice = int(input("Select any choice : "))

    if choice == 1:
        if is_locked:
            print("Can't add items. Cart is locked")
        else:
            item = input("Enter the item : ").lower()
            if item not in store:
                print(f"{item} is not in store")
            else:
                cart.append(item)
                print(f"{item} added to the cart")

    elif choice == 2:
        display_cart()

    elif choice == 3:
        if is_locked:
            print("Can't remove duplicates. Cart is locked.")
        else:
            cart = list(set(cart))
            print("Duplicates removed")
            print(f"Updated cart : {cart}")

    elif choice == 4:
        cart = tuple(cart)
        is_locked = True 
        print("Cart is now locked.")

    elif choice == 5:
        print("Thank you for using.")
        break

    else:
        print("Invalid choice")

    print("***********************************")
