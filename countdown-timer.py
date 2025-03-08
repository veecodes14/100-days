import time
import threading
import os 

def play_sound():
    os.system('afplay /System/Library/Sounds/Glass.aiff')

class CountdownTimer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        #conerting to seconds
        self.total_seconds = hours * 3600 + minutes * 60 + seconds
        self.remaining_seconds = self.total_seconds
        self.is_paused = False
        self.timer_thread = None

    def countdown(self):
        #countdown
        while self.remaining_seconds > 0:
            if self.is_paused:
                continue
            mins, secs = divmod(self.remaining_seconds, 60)
            hours, mins = divmod(mins, 60)
            timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            time.sleep(1)
            self.remaining_seconds -= 1

        self.notify_end()

    def start(self):
        if self.timer_thread is None:
            self.timer_thread = threading.Thread(target=self.countdown)
            self.timer_thread.start()

    def pause(self):
        self.is_paused = True
        print("\nTimer paused")

    def resume(self):
        self.is_paused = False
        print("\nTimer resumed")

    def reset(self):
        self.remaining_seconds = self.total_seconds
        print("\nTimer reset")
        self.start()

    def notify_end(self):
        print("\nTime's up!")
        os.system('afplay /System/Library/Sounds/Glass.aiff')

#user input
def user_input():
    try:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
    except ValueError:
        print("Invalid input. Enter integers only")
        return user_input()
    return hours, minutes, seconds

def main():
    hours, minutes, seconds = user_input()
    timer = CountdownTimer(hours, minutes, seconds)

    timer.start()

    while True:
        print("\nOptions: ")
        print("1. Pause")
        print("2. Resume")
        print("3. Reset")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            timer.pause()
        elif choice == '2':
            timer.resume()
        elif choice == '3':
            timer.reset()
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()