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
    sw = 80
    sh = 24
    # creates a new window and the border around it, listens for key strokes
    new_window = curses.newwin(sh + 1, sw + 1, 0, 0)
    new_window.border()
    new_window.keypad(True)
    # refreshes the terminal screen every 100 miliseconds
    new_window.timeout(100)

    # starting position of the Snake at left center of terminal screen
    # value turned to int so Snake can be drawn
    snakepos_x = int(sw / 4)
    snakepos_y = int(sh / 2)

    # three tuples for three starting parts of the Snake
    # starts with 'Y' value because origin of 'curse' box is top left corner
    snake = [
        # head
        (snakepos_y, snakepos_x),
        # middle
        (snakepos_y, snakepos_x - 1),
        # tail
        (snakepos_y, snakepos_x - 2),
    ]

    # defines the starting right movement of the Snake
    snake_start = curses.KEY_RIGHT

    """
    Main while loop that continues to run and execute for
    as long as the game is being played
    """
    while True:
        # creates a new instance of the Snake's head
        new_head = None

        # collision check on the border of the terminal screen
        # displays game over screen if Snake is at the edge of SW or edge of SH
        if snake[0][1] in (0, sw) or snake[0][0] in (0, sh):
            curses.endwin()
            print("GAME OVER!")
            quit()

        # listens for the 'Q' key press so the user can quit the terminal screen
        key = new_window.getch()
        if key == ord("q"):
            break
        # creates a new head of the Snake upon movement to the right
        if snake_start == curses.KEY_RIGHT:
            new_head = (snake[0][0], snake[0][1] + 1)
        
        # inserts a new head of the Snake at the correct location
        snake.insert(0, new_head)
        
        # gets rid of the last position of the Snake's tail
        tail_remove = snake.pop()
        new_window.addch(tail_remove[0], tail_remove[1], " ")

        # draws the new head of the Snake in the Python terminal
        # styles the Snake to a diamond shape
        new_window.addch(new_head[0], new_head[1], curses.ACS_DIAMOND)

"""
Wrapper allows to restore the terminal to a sane state
if the application raises an error
"""
curses.wrapper(main)