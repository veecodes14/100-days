#DAY-44 & 45
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

flavours = ['chocolate', 'vanilla', 'strawberry']
topping = ['biscoff', 'sprinkles', 'chocolate chip']

for one in flavours:
    for two in topping:
        print(one, 'topped with', two)

number = 0

while number < 5:
    print(number)
    if number == 6:
        continue
    number = number + 1
else:
    print("No longer < 5")