#DAY-28
def food_order(*args, **kwargs):
    #food items ordered
    #food = input("What would you like to have?: ")
    print("This is your food order: ")
    for item in args:
        print(f"- {item}")

    if kwargs:
        print("\nCustomizations: ")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    else:
        print("\nNo custoizations")

food = input("What would you like to have?: ").split(' ')
food_order(*food, **{"allergies": "no mushrooms", "delivery_notes": "bring it to apt 202"})

