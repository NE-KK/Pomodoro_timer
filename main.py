# Pomodoro timer
import time

def count_seconds():
    pass

def count_minutes():
    pass

if __name__ == "__main__":
    work_minutes = 25
    pause_minutes_short = 5
    pause_minutes_long = 20

    time_minutes = 0

    while time_minutes < work_minutes:

        time_seconds = 0
        while time_seconds < 60:
            time.sleep(1)
            print(f"{time_minutes} minuten : {time_seconds} sekunden")
            time_seconds += 1

        time_minutes += 1
