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


def greet():
    print("Hello, this is Jarvis your assistant\nHow can I assist you today?")


def dt():
    curr = datetime.now()
    now = datetime.strftime(curr, "%A")
    print(f"Today is {now}, {curr.strftime("%d %b %Y")}")


def time():
    curr = datetime.now()
    print(f"Time is {curr.strftime("%I:%M %p")}")


def open():
    site = input("Which site would like to open? ")
    group = re.search(r"(https?://)?(www\.)?(?P<name>.+)(\.com)?", site)
    if group:
        webbrowser.open(f"https://www.{group.group('name')}.com")
    else:
        print('Invalid site name')

'''feature of task manager :
    1.input the task
        -Task
        -Deadline
    2.add in the current task file
    3.when needed, show the task file displaying tasks
    4.delete the task when completed
    5.display a congratulation message when completed

    '''