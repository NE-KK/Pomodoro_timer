# Pomodoro timer
import time

def count_seconds(cs_time_seconds: int) -> str:
    seconds_countdown = 60 - cs_time_seconds

    if seconds_countdown == 60:
        return "00"
    elif seconds_countdown < 10:
        return str("0" + str(seconds_countdown))
    else:
        return str(seconds_countdown)

def count_minutes(cm_time_minutes: int, cm_pomodoro_time: int) -> str:
    cm_time_minutes = cm_pomodoro_time - cm_time_minutes

    if cm_time_minutes < 10:
        return str("0" + str(cm_time_minutes))
    else:
        return str(cm_time_minutes)

def set_pomodoro_phase(spp_pomodoro_counter):
    if spp_pomodoro_counter % 2 == 0:
        return "Work"
    else:
        return "Pause"

if __name__ == "__main__":
    is_running = True
    pomodoro_counter = 0
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
        string_minutes = count_minutes(time_minutes, pomodoro_array[pomodoro_counter])
        pomodoro_phase = set_pomodoro_phase(pomodoro_counter)

        print(f"{pomodoro_phase}:   {string_minutes} : {string_seconds}")

        if time_seconds == 0:
            pass

        time.sleep(1)
        time_seconds += 1

        if time_seconds == 60:
            time_seconds = 0
            time_minutes += 1

        # With a bug
        if string_minutes == "00" and string_seconds == "00":
            pomodoro_counter += 1