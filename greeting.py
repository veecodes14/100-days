def greet_user(**kwargs):
    
    name = kwargs.get('name', 'Guest')  
    age = kwargs.get('age', 'unknown')  
    
    print(f"Hello, {name}!")
    print(f"Your age is: {age}")


greet_user(name="Alice", age=25)
greet_user(name="Bob")
greet_user()