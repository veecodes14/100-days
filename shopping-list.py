# create a list of fruits
fruits = ["apple", "banana", "strawberry", "pawpaw"]

# add an element to the list
fruits.append("yooyi")

# insert an element at a specific position
fruits.insert(2, "mango")

# remove an element from the list
fruits.remove("banana")

# access elements by index
first_fruit = fruits[0]
last_fruit = fruits[-1]

# slice the list
some_fruits = fruits[1:4]  

# iterate through the list and print each fruit
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# display results
print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)
print("Some fruits:", some_fruits)