#DAY-14
# Define a list of students with their grades
students = [
    ("Kojo", [85, 90, 78]),
    ("Kobby", [92, 88, 79]),
    ("Adwoa", [95, 100, 89]),
    ("Yaa", [70, 75, 80]),
    ("Sam", [88, 92, 84]),
    ("Kwesi", [88, 92, 84]),
    ("Lisa", [78, 92, 70])
]

# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Display each student with their average grade
for student, grades in students:
    average = calculate_average(grades)
    print(f"{student}: Average Grade = {average:.2f}")
