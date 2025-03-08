def student_management_system():
    students = {}

    while True:
        print("\nWelcome to the Student Management System!")
        print("1. Add a Student")
        print("2. View All Students")
        print("3. View One Student")
        print("4. Remove Student")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == '1':
            name = input("Enter Name of Student: ")
            age = input("Enter Age of Student: ")
            grade = input("Enter Student's Grade: ")
            courses = input("Enter Student's Courses: ")
            students[name] = {"Age" : age, "Grade" : grade, "Courses" : courses}
            print(f"Student '{name}' added")

        elif option == '2':
            if students:
                for student in students:
                    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Course: {student['courses']}")
            else: 
                print("No Student Available at this Time")

        elif option == '3':
           name = input("Enter Name of Student to View: ")
           if name in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Course: {student['courses']}")
            else:
                print("Student not Found")

        elif option == '4':
            name = input("Enter Name of Student to Remove: ")
            if name in students:
                del student[name]
                print(f"Student '{name}' removed")
            else:
                print("Student Does not Exist")
            break

        else:
            print("Invalid Input. Select a Valid Option")

student_management_system()

               
                
        
        
        
       

