#DAY-32
import calendar

def display_calendar(year, month):
    print(calendar.month_name[month], year)
    print(calendar.month(year, month))

def main():
    print("Welcome to the Calender App!")

    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))

        if 1 <= month <= 12:
            display_calendar(year, month)
        else:
            print("Invalid entry. Enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Enter valid numbers for year and month.")

if __name__ == "__main__":
    main()
