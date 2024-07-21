tasks = []

def task():
    print("----WELCOME TO THE TASK MANAGEMENT ")

    a = int(input("Enter the number of tasks you want to perform: "))
    print("The number of tasks performing:", a)
    for i in range(1, a + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    print(f"Today's tasks are {tasks}")

    while True:
        operation = int(input("""Enter the Operation:
                        1>>FOR ADDING TASK
                        2>>FOR UPDATING THE TASK
                        3>>FOR REMOVING THE TASK
                        4>>TO VIEW ALL TASKS
                        5>>TO CLOSE THE PROGRAM
                        """))
        print(operation)

        if operation == 1:
            add = input("Enter the task to be added: ")
            tasks.append(add)
            print(f"Task {add} has been added to your list successfully..............")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                u = input("Enter new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = u
            else:
                print("Task not found.")

        elif operation == 3:
            d = input("Enter the task you want to delete: ")
            if d in tasks:
                tasks.remove(d)
                print(f"Task {d} has been removed successfully..............")
            else:
                print("Task not found.")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the program-----")
            break

        else:
            print("Invalid syntax. Please try again.")

task()