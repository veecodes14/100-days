#DAY-18
def contact_book():
    contacts = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contacts[name] = {'phone': phone, 'email': email}
            print(f"Contact '{name}' added")

        elif choice == '2':
            if contacts:
                print("\nContacts:")
                for name, info in contacts.items():
                    print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
            else: 
                print("No contacts available")

        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            if name in contacts:
                phone = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                contacts[name] = print(f"Contact '{name}' updated")

        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted")
            else:
                print(f"No contact with that name '{name}'.")

        elif choice == '5':
            print("Exiting contact book.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

contact_book()