try:
    numerator = input("Enter numerator: ")
    denominator = input("Enter denominator: ")
    division = int(numerator) / int(denominator)
    print(division)
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by 0")
except ValueError as e:
    print(e)
    print("Enter only numbers!")
except Exception as e:
    print(e)
    print("Something went wrong!")
