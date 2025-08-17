# Project 10: Simple Quiz game

questions = (
    "1. What is the result of print(10 % 3)?",
    "2. Which method is used to add an element to a list in Python?",
    "3. What is the data type of 5.0 in Python?",
    "4. True or False: In Python, lists are mutable.",
    "5. Which operator is used for floor division?"
)

options = (
    ("1. 1", "2. 2", "3. 3", "4. 0"),
    ("1. add()", "2. append()", "3. insert()", "4. push()"),
    ("1. int", "2. float", "3. str", "4. bool"),
    ("1. True", "2. False"),
    ("1. /", "2. //", "3. %", "4. **")
)

answers = ['1', '2', '2', '1', '2']  # Correct answers (as numbers in string format)

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your guess (1, 2, 3, 4): ").strip()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct ✅")
    else:
        print("Incorrect ❌")
        print(f"Correct answer: {answers[question_num]}")
    question_num += 1

print("\n🎯 Your final score:", score, "/", len(questions))
