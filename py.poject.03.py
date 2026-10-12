
print("Welcome to the Student Data Organizer!")

students = []
subjects = ["Math", "Science", "English", "History", "Art"]

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add Student
    if choice == "1":
        print("Enter student details:")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        student_subjects = input("Subjects: ")


        student = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Grade": grade,
            "DOB": dob,
            "Subjects": student_subjects
        }

        students.append(student)
        print("Student added successfully!")

    # 2. Display All Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("--- Display All Students ---")

            for student in students:
                print("Student ID:", student["ID"])
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Grade:", student["Grade"])
                print("Date of Birth:", student["DOB"])
                print("Subjects:", student["Subjects"])
                

    # 3. Update Student
    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        for student in students:
            if student["ID"] == student_id:
                student["Name"] = input("Enter new Name: ")
                student["Age"] = int(input("Enter new Age: "))
                student["Grade"] = input("Enter new Grade: ")
                student["DOB"] = input("Enter new Date of Birth: ")
                student["Subjects"] = input("Enter new Subjects: ")

                print("Student updated successfully!")
                break
        else:
            print("Student not found.")

    # 4. Delete Student
    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    # 5. Display Subjects
    elif choice == "5":
        print("Subjects Offered:")

        for subject in subjects:
            print(subject)

    # 6. Exit
    elif choice == "6":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please try again.")
