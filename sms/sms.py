students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    student = {'Roll': roll, 'Name': name, 'Course': course}
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("❌ No student records found.\n")
        return
    print("\n--- Student List ---")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Roll: {student['Roll']}, Name: {student['Name']}, Course: {student['Course']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student['Roll'] == roll:
            print(f"✅ Found: Roll: {student['Roll']}, Name: {student['Name']}, Course: {student['Course']}\n")
            return
    print("❌ Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student['Roll'] == roll:
            print("Leave blank to keep old value.")
            name = input("Enter new Name: ") or student['Name']
            course = input("Enter new Course: ") or student['Course']
            student['Name'] = name
            student['Course'] = course
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found.\n") 

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student['Roll'] == roll:
            students.remove(student)
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")

def menu():
    while True:
        print("📘 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

menu()
