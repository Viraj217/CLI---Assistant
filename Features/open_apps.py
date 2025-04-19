import subprocess

'''Open apps locally'''
def open_apps():
    app = input(">>> Enter the app you want to open (notepad, cmd, explorer, control, calc, snippingtool): ")
    subprocess.run([app])