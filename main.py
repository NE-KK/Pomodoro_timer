# Pomodoro timer
import time

def count_seconds(cs_time_seconds: int) -> str:
    if cs_time_seconds < 10:
        return str("0" + str(cs_time_seconds))
    else:
        return str(cs_time_seconds)

def count_minutes(cm_time_minutes: int) -> str:
    if cm_time_minutes < 10:
        return str("0" + str(cm_time_minutes))
    else:
        return str(cm_time_minutes)


if __name__ == "__main__":
    work_minutes = 25
    pause_minutes_short = 5
    pause_minutes_long = 20

    time_minutes = 0
    string_minutes = "00"
    string_seconds = "00"

    while time_minutes < work_minutes:

        time_seconds = 0
        while time_seconds < 60:
            time.sleep(1)

            string_seconds = count_seconds(time_seconds)

            print(f"{string_minutes} : {string_seconds}")
            time_seconds += 1

        time_minutes += 1
        string_minutes = count_minutes(time_minutes)
