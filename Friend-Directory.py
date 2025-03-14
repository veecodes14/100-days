#DAY-19
#Store Personal Details

def friend_directory():
    friends = {}

    while True:
        print("\n My Friends: ")
        print("1. Add Friend")
        print("2. View List of Friends")
        print("3. Update Information")
        print("4. Remove Friend")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            fav_color = input("Enter Favourite Color: ")
            friends[name] = {'age': age, 'Favourite Color': fav_color }
            print(f"Friend '{name}' added")

        elif choice == "2":
            if friends:
                print("\nFriend:")
                for name, info in friends.items():
                    print(f"Name: {name}, Age: {info['age']}, Favourite Color: {info['Favourite Color']}")
            else:
                print("No information available")

        elif choice == "3":
            name = input("Enter Name of Friend Whose Info to Update: ")
            if name in friends:
                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                fav_color = input("Enter New Favourite Color: ")
                friends[name] = {'age': age, 'Favourite Color': fav_color }
                print(f"Friend '{name} updated")  

        elif choice == "4":
            name = input("Enter Name of Friend to Remove: ")
            if name in friends:
                del friends[name]
                print(f"Friend '{name}' removed")
            else:
                print("Friend does not Exist")
                break
        
        else:
            print("Invalid. Please Select a Valid Option.")

friend_directory()

