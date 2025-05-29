class todolist:
    def __init__(self):
        self.task = []

    def add_task(self):
        task = input("Enter a task: ")
        self.task.append(task)
        print(f"Task '{task}' Added. ")

    def view_task(self):
        if not self.task:
            print("No task avlibale. ")
        else:
            print("Task: ")
            for i, task in enumerate(self.task,start = 1):
                print(f"{i}.{task}")

    def delete_task(self):
        if not self.task:
            print("No task avliable")
        else:
            self.view_task()
            task_number = input(input("Enter task number to delete")) -1
        
        if task_number<len(self.task):
            task = self.task.pop(task_number)
            print(f"Task '{task}' Delete.")
        else:
            print("Invalid task number")

    def run(self):
        while True:
            print("\nOptions: ")
            print("1.Add atsk ")
            print("2.View task ")
            print("3.Delet task ")
            print("4.Exit ")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("...EXIT...")
                break
            else:
                print("Invalid choice, pls try again..")

if __name__ == "__main__":
    todo = todolist()
    todo.run()