# Pomodoro timer
import time

work_minutes = 25
pause_minutes_short = 5
pause_minutes_long = 20

min_time = 0


while min_time < 5:

    sec_time = 0
    while sec_time < 60:
        time.sleep(1)
        print(f"{min_time} minuten : {sec_time} sekunden")
        sec_time += 1



    min_time += 1
