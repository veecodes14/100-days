#DAY-7
# primary and non-primary colors
primary_colors = ["red", "blue", "yellow"]  

# Function to check if a color is primary
def check_color(color):
    color = color.lower()  
    if color in primary_colors:
        print(color + " " + "is a primary color.")
    else:
        print(color + " " + "is not a primary color")

# Example of using the function
print("Welcome to the Primary vs Non-Primary Color Checker!")

# User Input
color_input = input("Enter a color to check: ")

check_color(color_input)
