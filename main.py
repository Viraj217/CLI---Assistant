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
    print("Type 'help' if you're confused.")
    print("Type 'stop' or 'exit' to shut me down.\n")

    while running:
        user_input = input(">>> ").strip().lower()

        if user_input in ["hello", "hi"]:
            print("Hello! How can I assist you today?")

        elif user_input == "help":
            print("\nHere's what I can help you with today:")
            print("🔹 Say hello")
            print("🔹 Show current time and date (type: date or time)")
            print("🔹 Open a website (type: open website)")
            print("🔹 Manage your tasks (type: task manager)")
            print("🔹 Set timers (type: set timer)")
            print("🔹 Show the current weather (type: weather)")
            print("🔹 Open apps installed on your system (type: open apps)\n")

        elif user_input == "time":
            display_time()

        elif user_input == "date":
            dt()

        elif user_input == "open website":
            open_browser()

        elif user_input == "set timer":
            timer()

        elif user_input == "weather":
            weather()

        elif user_input == "open apps":
            open_apps()

        elif user_input == "task manager":
            print("\n📋 Welcome to the Task Manager!")
            tm = Manager()
            tm.load()  # load any existing tasks

            print("You can add, remove, complete, update, and print your tasks.")
            print("Available commands: add, remove, complete, update, print, help, exit")

            while True:
                action = input("\n>>> Task Manager >> ").strip().lower()

                if action == "add":
                    tm.flush()
                    tm.load()
                    tm.add()
                    tm.save()

                elif action == "remove":
                    tm.flush()
                    tm.load()
                    tm.print()
                    tm.remove()
                    tm.save()

                elif action == "complete":
                    tm.flush()
                    tm.load()
                    tm.print()
                    tm.complete()
                    tm.save()

                elif action == "update":
                    tm.flush()
                    tm.load()
                    tm.print()
                    tm.update()
                    tm.save()

                elif action == "print":
                    tm.flush()
                    tm.load()
                    tm.print()

                elif action == "help":
                    print("Available commands: add, remove, complete, update, print, help, exit")

                elif action in ["stop", "exit", "close", "quit"]:
                    print("Exiting Task Manager.")
                    break

                else:
                    print("❌ Invalid command. Try again or type 'help'.")

        elif user_input in ["stop", "exit"]:
            print("Goodbye!")
            running = False

        else:
            print("⚠️ Sorry, I didn't understand that. Try 'help' to see what I can do.")

if __name__ == "__main__":
    main()
