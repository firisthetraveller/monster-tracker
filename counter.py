import time
from datetime import datetime
import json

from pynput.keyboard import Key, Listener, KeyCode, Controller

PRINTED = False
COUNTER = 0
TIMESTAMPS = []
MAP_TIMESTAMPS = []
MAPS = ["Herta: Seclusion Zone", "Herta: Supply Zone", "Herta: Storage Zone", "Herta: Base Zone",
        "Jarilo: Outlying Snow Plains", "Jarilo: Backwater Pass", "Jarilo: Corridor of Fading Echoes", "Jarilo: Everwinter Hill", "Jarilo: Great Mine", "Jarilo: Rivet Town", "Jarilo: Robot Settlement",
        "Xianzhou: Cloudford", "Xianzhou: Stargazer Navalia", "Xianzhou: Divination Commission", "Xianzhou: Artisanship Commission", "Xianzhou: Fyxestroll Garden", "Xianzhou: Alchemy Commission", "Xianzhou: Scalegorge Waterscape",
        "Penacony: Dream's Edge", "Penacony: A Child's Dream", "Penacony: The Reverie (Dreamscape)", "Penacony: Dewlight Pavillon", "Penacony: Clock Studios Theme Park", "Penacony: SoulGlad Scorchsand Audition Venue", "Penacony: Grand Theater"]
START_TIME = time.time()
KEYBOARD = Controller()

def usage():
    """
    This returns the basic help usage.
    """
    global PRINTED
    PRINTED = False
    return "Press:\n"\
        "\t- 'x' to count monsters.\n" \
        "\t- 'c' to mark map change.\n" \
        "\t- 'r' to restart recording without saving the current one.\n" \
        "\t- Esc to exit and save file.\n" \
        "The recording is saved in the output directory.\n"

def usage_extended():
    """
    This returns a more detailed help usage.
    """
    global PRINTED
    PRINTED = False
    return "Press:\n"\
        "\t- 'x' to count monsters.\n" \
        "\t- 'c' to mark map change.\n" \
        "\tWhen pressing 'c', if the current map is the last one, the recording will end and the file will be saved.\n" \
        "\t- 'r' to restart recording without saving the current one.\n" \
        "\t- Esc to exit and save file.\n" \
        "The recording is saved in the output directory.\n"

def delete_char_on_terminal():
    """
    For cleaning purposes, removes the character printed on the terminal when the user presses a letter.
    """
    print("\r\x1B[2K", end="")
    # \r : Return to beginning of current line
     # \x1B[2K : Erase line

def print_current_status():
    global PRINTED
    if PRINTED:
        # \x1B[F : Return to beginning of previous line
        # Remove the 3 lines of the previous (outdated) print
        print("\x1B[F\x1B[2K\x1B[F\x1B[2K\x1B[F\x1B[2K", end="")

    # Write the updated status
    print(f'Current map: {MAPS[len(MAP_TIMESTAMPS)]}\n' \
          f'Monster count: {COUNTER}\n' \
          f'Time: {datetime.fromtimestamp(time.time() - START_TIME).strftime("%M:%S.%f")}')
    PRINTED = True

def register_file():
    """
    Callable to save data into a file in the output directory.
    """
    run_time = time.time() - START_TIME

    # Just some info
    print(f'Fought {COUNTER} monsters in {run_time:.3f}s.')

    # The formatted data about to be saved
    json_dictionary = {
        "monster_count": COUNTER,
        "run_date": datetime.fromtimestamp(START_TIME).strftime("%a, %d %b %Y %H:%M:%S"),
        "run_time": datetime.fromtimestamp(run_time).strftime("%M:%S.%f"),
        "monster_time": TIMESTAMPS,
        "map_time": MAP_TIMESTAMPS
    }

    # Write in the output directory in a new file
    with open(f'output/recording_{int(START_TIME)}.txt', "a", encoding="utf-8-sig") as f:
        f.write(json.dumps(json_dictionary, indent=4))

def on_release(key):
    global START_TIME, TIMESTAMPS, MAP_TIMESTAMPS, COUNTER
    delete_char_on_terminal()
    if key == KeyCode.from_char('x'):
        COUNTER = COUNTER + 1
        TIMESTAMPS.append(f"{time.time() - START_TIME:.3f}")
        print_current_status()
    elif key == KeyCode.from_char('c'):
        MAP_TIMESTAMPS.append(f"{time.time() - START_TIME:.3f}")
        if (len(MAP_TIMESTAMPS) >= len(MAPS)):
            register_file()
            return False
        print_current_status()
    elif key == KeyCode.from_char('h'):
        print(usage_extended())
    elif key == KeyCode.from_char('r'):
        START_TIME = time.time()
        TIMESTAMPS = []
        MAP_TIMESTAMPS = []
        print("Recording reset.")
    elif key == Key.esc:
        # Stop listener
        register_file()
        return False

# Collect events until released
print("\nRecording started.\n")
print(usage())
with Listener(on_release=on_release) as listener:
    listener.join()