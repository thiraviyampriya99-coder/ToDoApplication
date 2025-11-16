# todo.py

TASK_FILE = "tasks.txt"  # This file will store all tasks permanently



def load_tasks():
    tasks = []
    try:

        with open(TASK_FILE, "r") as file:

            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:

        open(TASK_FILE, "w").close()
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)        # Add task to list
    save_tasks(tasks)         # Save updated list to file
    print("Task added successfully!")



def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")  # Print with numbering



def remove_task(tasks):
    view_tasks(tasks)         # Show available tasks
    if len(tasks) == 0:
        return

    try:
        index = int(input("\nEnter task number to remove: "))
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid option!")



def main():
    tasks = load_tasks()  # Load tasks initially

    while True:
        print("\n------ TO-DO LIST APP ------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option, try again!")


main()  # Start the program
