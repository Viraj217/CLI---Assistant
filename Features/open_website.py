import webbrowser
import re

def open_browser():
    site = input(">>> Which site would you like to open? ")
    words = tuple(site.split())
    for word in words:
        match = re.search(r"^(https?://)?(www\.)?(?P<name>[\w\-]+)(?P<middle>\.\w+)?(?P<domain>\.\w+)?$", word, re.IGNORECASE)
        if match:
            name = match.group('name')
            middle = match.group('middle') if match.group('middle') else ''
            domain = match.group('domain') if match.group('domain') else '.com'
            url = f"https://www.{name}{middle}{domain}"
            webbrowser.open(url)
            return
    print('Invalid site name')
