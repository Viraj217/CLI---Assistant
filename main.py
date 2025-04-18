'''This is the first file 
    I am making a basic CLI assistant'''

'''Basic feature:
    Say hello ☑️
    Show current time and date ☑️
    Open a website ☑️
    Task manager
    Set timers
    Show current weather
    Open files locally
    Play music           
    '''

from datetime import datetime
import webbrowser
import re
from tabulate import tabulate
import csv


def greet():
    print("Hello, this is Jarvis your assistant\nHow can I assist you today?")


def dt():
    curr = datetime.now()
    now = datetime.strftime(curr, "%A")
    print(f"Today is {now}, {curr.strftime("%d %b %Y")}")


def time():
    curr = datetime.now()
    print(f"Time is {curr.strftime("%I:%M %p")}")


def open_browser():
    site = input("Which site would like to open? ")
    group = re.search(r"(https?://)?(www\.)?(?P<name>.+)(\.com)?", site)
    if group:
        webbrowser.open(f"{group.group('name')}.com")
    else:
        print('Invalid site name')


'''feature of task manager :
    1.Input:
        -Task
        -Deadline
        -Priority
        -Status
    2.add in the current task file
    3.when needed, show the task file displaying tasks in the form a table
    4.delete the task when completed
    5.display a congratulation message when completed
    6.display the updated task list
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

    def remove(self):
        task_delete = input("Enter the task to delete: ")
        for task in self.tasks:
            if task.task == task_delete:
                self.tasks.remove(task)
                print(f"Task '{task_delete}' removed.")
                break

    def print(self):
        content = [[i+1, task.task, task.deadline, task.priority, task.status] for i, task in enumerate(self.tasks)]
        print(tabulate(content, headers=["No", "Task", "Deadline", "Priority", "Status"]))

    def complete(self):
        task_completed = input("Enter the task you completed: ")
        for task in self.tasks:
            if task.task == task_completed:
                task.status = "Completed"
                print(f"Task '{task_completed}' marked as completed.")
                break

    def update(self):
        task_to_update = input("Enter the task to update: ")
        for task in self.tasks:
            if task.task == task_to_update:
                update_what = input("What do you want to update? (task, deadline, priority, status): ")
                update_to = input(f"What is the new value for {update_what}? ")
                setattr(task, update_what, update_to)
                print(f"Task '{task_to_update}' updated.")
                break
    

    def load(self):
        with open('task.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                task = Task(row[0], row[1], row[2], row[3])
                self.tasks.append(task)

    def save(self):
        with open('task.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.task, task.deadline, task.priority, task.status])

manager = Manager()
manager.add()
manager.add()
manager.update()
manager.remove()
manager.print()
