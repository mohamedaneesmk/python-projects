# Project 9 : Student Grade Manager 

student_details = {}  # declared globally to use in the full code

def add_student():
    name = input("Enter your name: ")
    try:
        marks = int(input("Enter your marks: "))
        student_details[name] = marks
        print("✅ Student added!")
    except ValueError:
        print("❌ Please enter a valid number for marks.")

def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"
    
def display_student():
    if not student_details:
        print("No student details found.")
    else:
        for name, mark in student_details.items():
            grade = calculate_grade(mark)
            print(f"Name: {name:10} | Marks: {mark} | Grade: {grade}")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("❌ Please enter a valid choice.")
