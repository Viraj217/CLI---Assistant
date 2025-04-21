from word2number import w2n
import time
import winsound

'''Timer
    feature of timer:
    1. set a timer for a specific time
    2. when the time is up, display a message
    3. Display continuos time like a clock
'''
def timer():
    seconds = input(">>> Set a timer in seconds(with no floating points): ")
    if not seconds.isdigit():
        seconds = int(w2n.word_to_num(seconds))
    else:
        seconds = int(seconds)
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02}:{secs:02}"
        print(f"\rTime left: {timer_display}", end="")
        time.sleep(1)
        seconds -= 1
    print("\rTime's over!                                                           ") 
    winsound.Beep(1000, 1000)