def student_records():
    students = {}

    while True:
        print("\nWelcome to the Student Management System!")
        print("1. Add new students")
        print("2. Update existing student records")
        print("3. Calculate average grade of all students")
        print("4. Display all student records")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter name of student: ")
            age = input("Enter age of student: ")
            grade = input("Enter student's grade: ")
            students[name] = {'age': age, 'grade':grade}
            print(f"Student '{name}' added ")

        elif choice == '2':
            name = input("Enter name of student to update: ")
            if name in students:
                name = input("Enter new name: ")
                age = input("Enter updated age: ")
                grade = (input("Enter updated grade: ")).split()
                students[name] = {'age': age, 'grade': grade}
                print(f"Student: '{name}' updated")

        elif choice == '3':           
            all_grades = []
            for name, details in students.items():
                all_grades.append(int(details['grade']))
            average = sum(all_grades) / len(all_grades)
            print(f"Average Grade: {average:.2f}")
            
            
        elif choice == '4':
            if students:
                print("\nStudent: ")
                for name, info in students.items():
                    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
            else:
                print("No information available.")
                break

        else:
            print("Invalid. Choose a valid option.")

            

student_records()
 