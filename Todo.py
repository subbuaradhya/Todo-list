import os

FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def show(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

tasks = load_tasks()

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Added")

    elif choice == "2":
        show(tasks)

    elif choice == "3":
        show(tasks)
        n = int(input("Delete number: "))
        tasks.pop(n - 1)
        save_tasks(tasks)
        print("Deleted")

    elif choice == "4":
        break
