import json
import os

FILE_NAME = "data.json"

# Load data from file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data to file
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    name = input("Enter name: ")
    age = input("Enter age: ")
    roll = input("Enter roll number: ")
    mobile=input("Enter mobile.no:")

    student = {
        "name": name,
        "age": age,
        "roll": roll,
        "mobile":mobile
    }

    students.append(student)
    save_data(students)
    print("Student added successfully!")

# View students
def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)

# Search student
def search_student(students):
    mobile = input("Enter mobile number to search: ")

    for student in students:
        if student["mobile"] == mobile:
            print("Student found:", student)
            return

    print("Student not found.")

# Delete student
def delete_student(students):
    roll = input("Enter roll number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_data(students)
            print("Student deleted!")
            return

    print("Student not found.")

# Update student
def update_student(students):
    roll = input("Enter roll number to update: ")

    for student in students:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["mobile"]=input("Enter new mobile:")
            save_data(students)
            print("Student updated!")
            return

    print("Student not found.")

# Menu
def menu():
    students = load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

menu()