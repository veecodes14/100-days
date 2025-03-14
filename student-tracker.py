#DAY-13
student_tracker = ['Kojo', 'Kobby', 'Adwoa', 'Yaa']
print('The current list of students is: ' + str(student_tracker))
new_student = input('Enter a student name: ')
update = (new_student.split(','))

for i in update:
    student_tracker.append(i)


print(student_tracker)


