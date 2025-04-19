from tabulate import tabulate
import csv

'''Task Manager
    feature of task manager :
    1.Input:
        -Task
        -Deadline
        -Priority
        -Status
    2.add in the current task file
    3.when needed, show the task file displaying tasks in the form a table
    4.Update the status when completed
    5.remove the task from the list
    6.display a congratulation message when completed
    7.display the updated task list
'''

class Task:
    def __init__(self, task, deadline, priority, status):
        self.task = task
        self.deadline = deadline
        self.priority = priority
        self.status = status


class Manager:
    def __init__(self):
        self.tasks = []

    def add(self):
        task = input("Enter the task: ")
        deadline = input("Enter the deadline: ")
        priority = input("Enter the priority: ")
        status = input("Enter the status: ")
        new_task = Task(task, deadline, priority, status)
        self.tasks.append(new_task)
        print(f"Task '{task}' added.")

    def remove(self):
        task_delete = input("Enter the task to delete: ")
        for task in self.tasks:
            if task.task == task_delete:
                self.tasks.remove(task)
                print(f"Task '{task_delete}' removed.")
                break

    def print(self):
        content = [[i+1, task.task, task.deadline, task.priority, task.status] for i, task in enumerate(self.tasks)]
        print(tabulate(content, headers=["No", "Task", "Deadline", "Priority", "Status"], tablefmt="grid"))

    def complete(self):
        task_completed = input("Enter the task you completed: ")
        for task in self.tasks:
            if task.task == task_completed:
                task.status = "Completed"
                print(f"Task '{task_completed}' marked as completed.")
                break

    def update(self):
        task_to_update = input(">>> Enter the task to update: ")
        for task in self.tasks:
            if task.task == task_to_update:
                update_what = input("What do you want to update? (task, deadline, priority, status): ")
                update_to = input(f"What is the new value for {update_what}? ")
                setattr(task, update_what, update_to)
                print(f"Task '{task_to_update}' updated.")
                break
            else:
                print("Task not found. Please check the task name.")
    
    def load(self):
        try:
            with open('task.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row['Task'], row['Deadline'], row['Priority'], row['Status'])
                    self.tasks.append(task)
        except FileNotFoundError:
            print("Please add a task first.")

    def save(self):
        with open('task.csv', 'w', newline='') as file:
            fieldnames = ["Task", "Deadline", "Priority", "Status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow({
                    "Task": task.task,
                    "Deadline": task.deadline,
                    "Priority": task.priority,
                    "Status": task.status
                })
            self.tasks.clear()

