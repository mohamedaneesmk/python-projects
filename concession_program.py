# Project 2: Concession program using dictionary

menu = {
    "idly":10,
    "dosa":15,
    "puri":20,
    "chappathi":15,
    "parotta":15,
    "upma":30
}

cart = []
total = 0
# print(menu)
print("------------MENU CARD-----------")
for key,value in menu.items():
    print(f"{key:9} : ₹{value}")


while True:
    food  = input("Select an item (Q to Quit) : ").strip().lower()
    print(menu.get(food))
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        total += menu.get(food) 
    else:
        print(f"{food} is not found in the list.")

print("Cart : ",cart)
print(f"Total : ₹{total}")
