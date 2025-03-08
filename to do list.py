import json

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """load tasks from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return[]
        
    def save_tasks(self):
        """save tasks to a JSON"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        """add a new task to the list"""
        self.tasks.append(task)
        self.save_tasks()
        print("task added")

    def view_tasks(self):
        """display all tasks in the list"""
        if not self.tasks:
            print("no tasks in the list")
            return
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def remove_task(self, task_index):
        """remove a task from the list (by index)"""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Removed task: {removed_task}")
        else: 
            print("Invalid task number.")

    def main(self):
        """user interaction"""
        while True:
            print("\nTo-Do List")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Exit")
                
            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)

            elif choice == '2':
                self.view_tasks()

            elif choice == '3':
                self.view_tasks()
                task_index = int(input("Enter the task number to remove: ")) - 1
                self.remove_task(task_index)

            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Task not found. Try again")

if __name__ == "__main__":  
    todo_list = ToDoList()
    todo_list.main()  
