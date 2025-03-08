def valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please choose from", valid_options)

def register():
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be a positive number.")

        is_student = valid_input("Are you a student of this school? (yes/no)? ", ["yes", "no"])
        courses_completed = valid_input("Have you completed the necessary courses (yes/no)? ", ["yes", "no"])

        if age >= 18:
            if is_student == "yes":
                if courses_completed == "yes":
                    print("Registration successful! Welcome back to school.")
                elif courses_completed == "no":
                    print("You cannot register until you complete last semester's courses.")
            elif is_student == "no":
                print("Sorry, only students can register for this course.")
        elif age < 18:
            print("You must be at least 18 years old to register for this course.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


register()