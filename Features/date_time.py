from datetime import datetime


'''Date and time'''
def dt():
    curr = datetime.now()
    now = datetime.strftime(curr, "%A")
    print(f"Today is {now}, {curr.strftime("%d %b %Y")}")


def display_time():
    curr = datetime.now()
    print(f"Time is {curr.strftime("%I:%M %p")}")