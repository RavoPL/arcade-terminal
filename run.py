"""
Imports the 'curses' built-in Python library which can be used to create
a terminal-independent screen-painting and key-handling facility
"""
import curses

"""
Main function that sets the bounding box border
as well as the details of the Snake and keyboard input
"""
def main(stdscr):
    # clears the screen at game start
    stdscr.clear()
    # disables the blinking of the cursor in terminal
    curses.curs_set(0)
    # sets the screen width and screen height of the bounding box
    sw = 70
    sh = 20


"""
Wrapper allows to restore the terminal to a sane state
if the application raises an error
"""
curses.wrapper(main)