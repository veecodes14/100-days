# Tuple of student names 
students_tuple = ("Kojo", "Kobby", "Adwoa", "Yaa", "Sam", "Kwesi")
print("Students Tuple:", students_tuple)

# Set of students who passed 
passed_students = {"Kojo", "Kobby", "Adwoa", "Lisa", "Sam"}
print("Passed Students Set:", passed_students)

# Adding a new student who passed
passed_students.add("Ama")
print("Passed Students after adding Ama:", passed_students)

# Checking if a student passed
print("Did Kobby pass?", "Kobby" in passed_students)

# Finding the students who didn't pass
failed_students = set(students_tuple) - passed_students
print("Failed Students:", failed_students)
