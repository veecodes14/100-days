#DAY-35 & 36
def verify_pin(correct_pin):
    for attempt in range(3):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == correct_pin:
            return True
        print("Incorrect PIN. Try again.")
    print("Too many incorrect attempts. Exiting.")
    return False 


def deposit(balance, transactions):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def withdraw(balance, transactions, min_balance):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and (balance - amount) >= min_balance:
            balance -= amount
            transactions.append(f"Withdrew: ${amount:.2f}") #I used AI for these to provide the right format
            print(f"Successfully withdrew ${amount:.2f}")
        else:
            print("Insufficient funds or minimum balance requirement not met.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def check_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def view_transactions(transactions):
    if transactions:
        print("\nTransaction History:")
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions yet.")

def atm():
    pin = "1234"
    min_balance = 1000
    balance = 1000
    transactions = []

    if not verify_pin(pin):
        return

    while True:
        print("\nATM Menu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            balance = deposit(balance, transactions)
        elif choice == "2":
            balance = withdraw(balance, transactions, min_balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            view_transactions(transactions)
        elif choice == "5":
            print("Exiting ATM. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

atm()
