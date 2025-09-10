# Student Management System with File Storage (CSV)
import csv
import os

FILENAME = "students.csv"
students = {}

# Load existing data from file (if any)
def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    roll, name, age, course = row
                    students[roll] = {"Name": name, "Age": age, "Course": course}

# Save all data back to file
def save_data():
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for roll, info in students.items():
            writer.writerow([roll, info["Name"], info["Age"], info["Course"]])

def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("❌ Roll Number already exists!\n")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    students[roll] = {"Name": name, "Age": age, "Course": course}
    save_data()
    print("✅ Student Added Successfully!\n")

def search_student():
    roll = input("Enter Roll Number to Search: ")
    if roll in students:
        print(f"\n📌 Student Found (Roll: {roll})")
        for key, value in students[roll].items():
            print(f"{key}: {value}")
        print()
    else:
        print("❌ Student Not Found.\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    if roll in students:
        del students[roll]
        save_data()
        print("✅ Student Deleted Successfully!\n")
    else:
        print("❌ Student Not Found.\n")

def display_all():
    if students:
        print("\n--- All Student Records ---")
        for roll, info in students.items():
            print(f"Roll: {roll}, Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}")
        print()
    else:
        print("No records found.\n")

def main():
    load_data()  # Load data at the start
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            display_all()
        elif choice == '5':
            print("👋 Exiting Student Management System. Goodbye!")
            break
        else:
            print("❌ Invalid Choice! Try Again.\n")

if __name__ == "__main__":
    main()
