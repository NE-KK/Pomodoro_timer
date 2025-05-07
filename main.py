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

def set_pomodoro_phase():
    return "Work"

if __name__ == "__main__":
    is_running = True
    work_minutes = 25
    pause_minutes_short = 5
    pause_minutes_long = 20

    time_seconds = 0
    time_minutes = 0
    string_minutes = "00"
    string_seconds = "00"

    pomodoro_array = [work_minutes, pause_minutes_short,
                      work_minutes, pause_minutes_short,
                      work_minutes, pause_minutes_short,
                      work_minutes, pause_minutes_long]


    while is_running:
        string_seconds = count_seconds(time_seconds)
        string_minutes = count_minutes(time_minutes)
        pomodoro_phase = set_pomodoro_phase()

        print(f"{pomodoro_phase}:   {string_minutes} : {string_seconds}")

        time.sleep(1)
        time_seconds += 1

        if time_seconds == 60:
            time_seconds = 0
            time_minutes += 1

