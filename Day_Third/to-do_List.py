#this is my third day project for 30 days 30 projects so today we are going to build a todo list using it so lets go 

task = []  # List to store tasks

def add_task():
    new_task = input("Enter the name of your task: ")
    task.append(new_task)
    print(f"Task added: {new_task}")
    print(f"Current Tasks: {task}")


def remove_task():
    print("Current Tasks:", task)
    rm_task = input("Which task do you want to remove (Enter task name): ")
    if rm_task in task:
        task.remove(rm_task)
        print(f"Task removed: {rm_task}")
    else:
        print(f"Task '{rm_task}' not found.")


def view_task():
    if not task:
        print("No tasks to display.")
    else:
        print("Current Tasks:")
        for i, task_item in enumerate(task, 1):
            print(f"{i}. {task_item}")


def mark_task():
    print("Current Tasks:", task)
    if task:
        task_number = int(input("Which task number you want to mark as done: "))
        if 1 <= task_number <= len(task):
            task[task_number - 1] += " - Done"
            print(f"Task '{task[task_number - 1]}' marked as done.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to mark as done.")


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task_item in task:
            file.write(task_item + "\n")
    print("Tasks saved.")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            task.clear()  # Clear the current task list before loading
            for line in file:
                task.append(line.strip())
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found.")
    except Exception as e:
        print(f"An error occurred while loading tasks: {e}")


def menu():
    print("\n" + "=" * 30)
    print(" Welcome to TO-DO List Manager! ")
    print("=" * 30)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Mark Task as Done")
    print("5. Save and Exit")
    print("6. Load Tasks")
    print("=" * 30)

while True:
    try:
        menu()
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            view_task()
        elif choice == 4:
            mark_task()
        elif choice == 5:
            save_tasks()
            print("Thanks for using TO-DO List Manager! Goodbye!")
            break

        elif choice == 6:
            load_tasks()
        else:
            print("Invalid choice! Please choose a valid option.")

    except ValueError:
        print("Please enter a valid number.")
