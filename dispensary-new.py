#DAY-38-41
class User:
    
    def __init__(self, pin):
        self.pin = pin

    def verify_pin(self):
        for attempt in range(3): #user has 4 attempts
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                return True
            print("Incorrect PIN, try again!")
        print("Too many incorrect attempts.")
        return False


class Medicine:
    
    def __init__(self, name, origin, SN, available):
        self.name = name
        self.origin = origin
        self.SN = SN
        self.available = available

    def check_status(self):
        status = "Available" if self.available else "Out of Stock"
        print(f"{self.name} - Status: {status}")

    def get_prescription(self):
        if not self.available:
            print(f"Prescription for {self.name} has been generated.")
        else:
            print(f"{self.name} is available; no prescription needed.")

    def display_info(self):
        status = "Available" if self.available else "Get Prescription"
        print(f"\nName: {self.name}\nOrigin: {self.origin}\nSN: {self.SN}\nStatus: {status}") 


class Dispensary:

    
    def __init__(self):
        self.medicines = {
            "Paracetamol": Medicine("Paracetamol", "China", 100, True),
            "Tramadol": Medicine("Tramadol", "Cuba", 101, False),
            "Imodium": Medicine("Imodium", "United Kingdom", 102, True),
        } #dictionary for medicines

    def menu(self):
        while True:
            print("\nDispensary Menu")
            print("1. Check Status of Medicine")
            print("2. Get Prescription")
            print("3. Display Medicine Info")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice in ['1', '2', '3']:
                med_name = input("Enter the medicine name: ").strip() #cleaning the input
                if med_name in self.medicines:
                    medicine = self.medicines[med_name]

                    if choice == '1':
                        medicine.check_status()
                    elif choice == '2':
                        medicine.get_prescription()
                    elif choice == '3':
                        medicine.display_info()
                else:
                    print("Medicine not found.")

            elif choice == '4':
                print("Exiting system.")
                break

            else:
                print("Invalid option. Try again.")


# Main Execution
def main():
    user = User(pin="1234")  # Default PIN
    dispensary = Dispensary()

    if user.verify_pin():
        dispensary.menu()


main()

