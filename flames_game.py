# Project 10 : Flames Game 

def flames_game(name1,name2):
    # Step 1: Clean names
    name1 = name1.replace(" ","").lower()
    name2 = name2.replace(" ","").lower()

    # Step 2: Remove common letters
    name1_list = list(name1)
    name2_list = list(name2)

    for char in name1[:]:
        if char in name2_list:
            name1_list.remove(char)
            name2_list.remove(char)
    
    # Step 3: Count remaining letters
    count =len(name1_list) + len(name2_list)

    # Step 4: FLAMES elimination
    flames = ["F","L","A","M","E","S"]
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index+1:] + flames[:split_index]
        else:
            flames.pop()

    # Step 5: Relationship mapping
    relationships = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Siblings"
    }

    return relationships[flames[0]]

def main():
    your_name = input("Enter your name = ")
    crush_name = input("Enter your crush's name = ")
    result = flames_game(your_name,crush_name)
    print(f"Flames result = {result}")

if __name__ == "__main__":
    main()