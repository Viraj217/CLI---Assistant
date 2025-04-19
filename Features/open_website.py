import webbrowser
import re

'''Visiting any site'''
def open_browser():
    site = input("Which site would like to open? ")
    group = re.search(r"(https?://)?(www\.)?(?P<name>.+)(\.com)?", site)
    if group:
        webbrowser.open(f"{group.group('name')}.com")
    else:
        print('Invalid site name')