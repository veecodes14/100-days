#DAY-20
def book_library():
    books = {}

    while True:
        print("\nWelcome to Your Book Library")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. View All Books")
        print("4. Exit Library")

        choice = input("Enter an Option (1-4): ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            books[title] = {'Title': title, 'Author': author}
            print(f"Book '{title}' added")

        elif choice == "2":
            title = input("Enter Title of Book to Remove: ")
            if title in books:
                del books[title]
                print(f"Book '{title}' removed")
            else:
                print("Invalid Entry")
                break

        elif choice == "3":
            if books:
                print("\nBook:")
                for title, info in books.items():
                    print(f"Title: {title}, Author: {author}")
            else:
                print("Book Not Found") 

        elif choice == "4":
            print("Exiting Library")
            break

        else: 
            print("Invalid. Select a Valid Option")

book_library()
