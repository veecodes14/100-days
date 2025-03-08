import random
# Number Game
print("Do you want to play a game?" )
response = input("Yes or No?: ")
random_number = random.randint(1, 1000)

if response == "Yes":    
    guess = input("What number am I thinking about from 1 to 1000?: ")
    if guess == random_number:
        print("Good job!")
    else: 
        print("Try again, the number is " + str(random_number))
else: print("Too bad")

