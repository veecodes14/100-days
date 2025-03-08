def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract (a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} * {b}")
    return a / b

print("quick math")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#puzzle
print("here's a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("that becomes: ", what, "can you do it by hand?")


