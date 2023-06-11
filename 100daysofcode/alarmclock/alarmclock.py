from playsound import playsound
import time

clear = "\033[2J"
clear_and_return = "\033[H"
def alarm(seconds):
    time_elapsed = 0
    print(clear)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{clear_and_return}alarm will sound in : {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

minutes = int(input("how many minutes to wait: "))
seconds = int(input("how many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)


