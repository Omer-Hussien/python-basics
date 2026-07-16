
students = []

def display_menu():
    print("=======Student Management System=======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print('---------------------------------------')



def add_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    major = input("Enter Major: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    }

    students.append(student)

    print("Student added successfully.")


def view_student():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n========== Students ==========")

    for student in students:
        print(f"ID    : {student['id']}")
        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"Major : {student['major']}")
        print("-" * 30)

def search_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print(f"ID    : {student['id']}")
            print(f"Name  : {student['name']}")
            print(f"Age   : {student['age']}")
            print(f"Major : {student['major']}")
            return

    print("Student not found.")


def update_student():
    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print("Leave blank to keep current value.")

            new_name = input(f"Name ({student['name']}): ")
            new_age = input(f"Age ({student['age']}): ")
            new_major = input(f"Major ({student['major']}): ")

            if new_name != "":
                student["name"] = new_name

            if new_age != "":
                student["age"] = new_age

            if new_major != "":
                student["major"] = new_major

            print("Student updated successfully.")
            return

    print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")

def main():

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
