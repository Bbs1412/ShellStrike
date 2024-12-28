# Theme: `Dark visual studio` -> `One dark pro monokai darker`
# Installed `Python Extension Pack`

import os
from time import sleep
import random


LINE_UP_CHAR = "\033[F"
CLEAR_LINE_CHAR = "\033[K"
GO_TO_START_CHAR = "\r"
TERMINAL_WIDTH = os.get_terminal_size().columns
STEP = 3


# List of different colors
COLOR_LIST = [
    "\033[32m",             # Green
    "\033[33m",             # Yellow
    "\033[34m",             # Blue
    "\033[35m",             # Magenta
    "\033[36m",             # Cyan
]

GUN_COLOR = "\033[31m"      # Red color
RESET_COLOR = "\033[0m"     # Reset color
BULLET_COLOR = "\033[31m"   # Red color
CAR_COLOR = "\033[31m"      # Red color


original = """{bullet_color}
{spc} :{GUN_color}
{spc} ^
{spc}/*\\
{spc}---{reset_color}
"""

fighter_jet = """{bullet_color}
{spc}          ●{GUN_color}
{spc}        __|__
{spc}--@--@--|   |--@--@--
{spc}        /_@_\{reset_color}
"""

jet = """{bullet_color}
{spc}       *{GUN_color}
{spc}     __|__
{spc}--@-@-(_)-@-@--{reset_color}
"""


supersonic = """{bullet_color}
{spc}          ●●   {GUN_color}
{spc}        __|__
{spc}--@--@--|___|--@--@-- 
{spc}        /___\\{reset_color}
"""

heavy_military_plane = """{bullet_color}
{spc}     ●       ●   {GUN_color}
{spc}         ^      {GUN_color}
{spc}     | / | \\ |
{spc}    _|_|_|_|_|_
{spc}==@==@==(_)==@==@== 
{spc}  |_____________| {reset_color}
"""

heavy_military_plane_2 = """{bullet_color}
{spc}     ▲       ▲   {GUN_color}
{spc}         ^      {GUN_color}
{spc}     | / | \\ |
{spc}    _|_|_|_|_|_
{spc}==@==@==(_)==@==@== 
{spc}  |_____________| {reset_color}
"""

# {spc}       ✈  {GUN_color}
advanced_fighter_jet = """{bullet_color}
{spc}           ✦  {GUN_color}
{spc}         __|__
{spc}--@--✦--|  ✈  |--✦--@--
{spc}         /¯¯¯\{reset_color}
"""

heavy_bomber = """{bullet_color}
{spc}     💥  +  💥   {GUN_color}
{spc}     |___|___|
{spc}==@==@==(_)==@==@==
{spc}      |█████|{reset_color}
"""


def pick_random_color():
    return random.choice(COLOR_LIST)


def calc_offset(x):
    lines = x.split('\n')
    max_len_of_row = 0
    for l in lines:
        max_len_of_row = max(max_len_of_row, len(l))
    return max_len_of_row


all_GUNs = [
    (original, calc_offset(original)),
    (jet, calc_offset(jet)),
    (fighter_jet, calc_offset(fighter_jet)),
    (supersonic, calc_offset(supersonic)),
    (heavy_military_plane, calc_offset(heavy_military_plane)),
    (heavy_military_plane_2, calc_offset(heavy_military_plane_2)),
    (advanced_fighter_jet, calc_offset(advanced_fighter_jet)),
    (heavy_bomber, calc_offset(heavy_bomber))
]

GUN, OFFSET = all_GUNs[0]
CURR_GUN = 0


def change_GUN():
    global GUN, OFFSET, CURR_GUN

    CURR_GUN = (CURR_GUN + 1) % len(all_GUNs)
    GUN, OFFSET = all_GUNs[CURR_GUN]
    # GUN, OFFSET = all_GUNs[-1]


if GUN[-1] == '\n':
    GUN = GUN[:-1]
if GUN[0] == '\n':
    GUN = GUN[1:]

right_dir = True
curr_pos = 2
last_pos = curr_pos


print("\n"*50)

try:
    while (True):
        last_pos = curr_pos

        if right_dir and curr_pos < TERMINAL_WIDTH - OFFSET:
            curr_pos += STEP
        elif right_dir:
            right_dir = False
            BULLET_COLOR = pick_random_color()
            CAR_COLOR = pick_random_color()
            change_GUN()

        if not right_dir and curr_pos > STEP:
            curr_pos -= STEP
        elif not right_dir:
            right_dir = True
            BULLET_COLOR = pick_random_color()
            CAR_COLOR = pick_random_color()

        lines = GUN.count("\n")

        #  if you want to keep last line empty (always):
        #    # end the GUN print with '\n'
        #    # erase the (lines-1) in the loop
        # else:
        #    # end the GUN print with '' or '\r'
        #    # erase the (lines) in the loop

        print(GUN.format(
            spc=" " * curr_pos,
            bullet_color=BULLET_COLOR,
            GUN_color=CAR_COLOR,
            reset_color=RESET_COLOR
        ), end='\r')

        iteration_gap = 0.1
        sleep(iteration_gap / 2)

        for i in range(lines-1):
            print(CLEAR_LINE_CHAR, LINE_UP_CHAR,  sep='', end='\r')

        sleep(iteration_gap / 2)
        # print(' ' * last_pos, f'{BULLET_COLOR}:{RESET_COLOR}')


except KeyboardInterrupt:
    print()
    print(GUN.format(
        spc=" " * curr_pos,
        bullet_color=BULLET_COLOR,
        GUN_color=CAR_COLOR,
        reset_color=RESET_COLOR
    ))
    print("\nExiting...")
    exit(0)
