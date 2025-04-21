'''This is the first file 
    I am making a basic CLI assistant'''

'''Basic feature:
    Say hello ☑️
    Show current time and date ☑️
    Open a website ☑️
    Task manager ☑️
    Set timers ☑️
    Show current weather ☑️
    Open apps locally ☑️   
    '''

from Features.greet import greet
from Features.timer import timer
from Features.open_apps import open_apps
from Features.task_manager import Manager
from Features.weather import weather
from Features.date_time import dt, display_time
from Features.open_website import open_browser

def main():
    running = True

    greet()
    print("Type help if confused.")
    print("Type 'stop' or 'exit' to shut me down.\n")
    while running:
        user_input = input(">>> ").strip().lower()
        if user_input.lower() in ["hello", "hi"]:
            print("Hello! How can I assist you today?")


        elif user_input.lower() == "help":
            print("Here's what I can help you with today:\n")
            print("🔹 Say hello")
            print("🔹 Show current time and date: date or time")
            print("🔹 Open a website: open website")
            print("🔹 Manage your tasks: task manager")
            print("🔹 Set timers: set timer")
            print("🔹 Show the current weather: weather")
            print("🔹 Open apps installed on your system: open apps")
            print("How can I assist you? 🤖")


        elif user_input.lower() == "time":
            display_time()


        elif user_input.lower() == "date":
            dt()


        elif user_input.lower() == "open website":
            open_browser()


        elif user_input.lower() == "task manager":
            print("Welcome to the Task Manager!")
            tm = Manager()
            print("You can add, remove, complete, update, and display tasks. (help, add, print, remove, complete, update)\nTo exit write 'stop' or 'exit'")
            while True:
                what_todo=input(">>> What would you like to do? ").lower().strip()
                if what_todo == "add":
                    tm.add()
                    tm.print()
                    tm.save()

                elif what_todo == "remove":
                    tm.load()
                    if not tm.load():
                        print("Add a task first.")  
                        continue
                    tm.remove()
                    tm.print()
                    tm.save()

                elif what_todo == "complete":
                    tm.load()
                    if not tm.load():  
                        print("Add a task first.")
                        continue
                    tm.print()
                    tm.complete()
                    tm.print()
                    tm.save()

                elif what_todo == "update":
                    tm.load()
                    if not tm.load(): 
                        print("Add a task first.")
                        continue
                    tm.print()
                    tm.update()
                    tm.print()
                    tm.save()

                elif what_todo == "print":
                    tm.load()
                    if not tm.load():
                        print("Add a task first.")
                        continue
                    tm.print()
                    tm.save()

                elif what_todo == "help":
                    print("You can add, remove, complete, update, print.")

                elif what_todo in ["stop", "exit", "close", "quit"]:
                    print("Exiting Task Manager.")
                    break

                else:
                    print("Invalid option. Please try again.")


        elif user_input.lower() == "set timer":
            timer()


        elif user_input.lower() == "weather":
            weather()


        elif user_input.lower() == "open apps":
            open_apps()


        elif user_input.lower() in ["stop", "exit"]:
            print("Goodbye!")
            running = False


        else:
            print("I'm sorry, I didn't understand that.")
            print("Please try again.")

if __name__ == "__main__":
    main()