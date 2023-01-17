"""
Imports the 'Curses' built-in Python library with the texpad widget
which can be used to create a rectangular bounding box within the terminal
"""
import curses
from curses import textpad

"""
Main function that sets the bounding box border
as well as the details of the Snake and keyboard input
"""
def main(stdscr):
    # disables the blinking of the cursor in terminal
    curses.curs_set(0)