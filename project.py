# Student Record Management System (SRMS)

students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student already exists.")
        return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))

    students[student_id] = {
        "name": name,
        "department": department,
        "cgpa": cgpa
    }

    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return

    for student_id, details in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Department: {details['department']}")
        print(f"CGPA: {details['cgpa']}")

def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        details = students[student_id]
        print(f"\nName: {details['name']}")
        print(f"Department: {details['department']}")
        print(f"CGPA: {details['cgpa']}")
    else:
        print("Student not found.")

def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        name = input("Enter new name: ")
        department = input("Enter new department: ")
        cgpa = float(input("Enter new CGPA: "))

        students[student_id] = {
            "name": name,
            "department": department,
            "cgpa": cgpa
        }

        print("Student record updated.")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student record deleted.")
    else:
        print("Student not found.")

def main_menu():
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()