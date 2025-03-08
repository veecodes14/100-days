# simple calculator
print("Welcome to simple calculator. ")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
operator = input("Enter operation: ")
first_number = input("Enter first number: ")
second_number = input("Enter second number: ") 

if operator == "1":
    result = int(first_number) + int(second_number) 
elif operator == "2":
    result = int(first_number) - int(second_number) 
elif operator == "3":
    result = int(first_number) * int(second_number) 
elif operator == "4":
    result = int(first_number) / int(second_number) 
else:
    print("Operation not valid")

answer = str(result)
print("The result is " + answer)