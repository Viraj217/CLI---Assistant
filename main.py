'''This is the first file 
    I am making a basic CLI assistnt'''

'''Basic feature:
    Say hello ☑️
    Show current time and date ☑️
    Open a website ☑️
    Task manager
    Set timers
    Show current weather'''

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
    1.input the task
        -Task
        -Deadline
    2.add in the current task file
    3.when needed, show the task file displaying tasks in the form a table
    4.delete the task when completed
    5.display a congratulation message when completed
    6.display the updated task list
    '''


def add_task():
    task = input("Enter the task: ")
    deadline = input("Enter the deadline: ")

    # Open the file and add the task with deadline
    with open("tasks.csv", "r", newline='') as file:
        # header for the dictionary of the csv file
        reader = csv.DictReader(file)
        rows = list(reader)

    with open("tasks.csv", "a", newline='') as file:
        h = ['Task', 'Deadline']
        writer = csv.DictWriter(file, fieldnames=h)

        if not rows:
            # if the file is empty, write the header
            writer.writeheader()

        writer.writerow({'Task': task, 'Deadline': deadline})
    print("Task added successfully!")
    print("Updated task list:\n")
    print_tasks()


def complete():
    pass
    # task = input("Enter the task you completed: ")
    # # with open("tasks.csv", "r") as f:

    # print(f"Congratulations on completing {task}!")
    # print("Updated task list:")
    # print_tasks()


def print_tasks():
    with open("tasks.csv", newline='') as f:
        tasks = csv.DictReader(f)
        for i in range(2)q:
            content = list(tasks[i].values())
        print(content)
        # if not content:
        #     print("No tasks found.")
        # else:
        #     content = [row for row in tasks]
        #     print(tabulate(content,headers="keys" ,tablefmt="grid"))
        print(content)

add_task()
add_task()
# complete()