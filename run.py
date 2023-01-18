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
    """
    stdscr.nodelay(1)
    """
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

    # creates the initial apple centered in the middle of the screen, styles it to a degree symbol
    apple = (int(sw/2), int(sh/2))
    new_window.addch(apple[0], apple[1], curses.ACS_DEGREE)
    
    # defines the starting right movement of the Snake
    snake_move = curses.KEY_RIGHT

    """
    Main while loop that continues to run and execute for
    as long as the game is being played
    """
    while True:
        # creates a new, empty instance of the Snake's head
        new_head = None

        # collision check on the border of the terminal screen
        # displays game over screen if Snake is at the edge of SW or edge of SH
        if snake[0][1] in (0, sw) or snake[0][0] in (0, sh):
            game_over = "GAME OVER! You collided with the wall! Press 'Q' to exit"
            new_window.addstr(int(sh//2), int(sw//2) - len(game_over)//2, game_over)
            new_window.nodelay(0)
            new_window.getch()
            quit()
        # displays game over screen if Snake's head collides with any other body part
        if snake[0] in snake[1:]:
            ate_self = "GAME OVER! You ate your own tail! Press 'Q' to exit"
            new_window.addstr(int(sh//2), int(sw//2) - len(ate_self)//2, ate_self)
            new_window.nodelay(0)
            new_window.getch()
            quit()

        # listens for the 'Q' key press so the user can quit the terminal screen
        key = new_window.getch()
        if key == ord("q"):
            break

        # allows for continuous movement of Snake
        """
        if key == -1:
            snake_move = snake_move
        else:
            snake_move = key
        """
        
        # listens for key input on arrow keys, which will change movement of Snake
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            snake_move = key
        
        # current, active head of the Snake
        head = snake[0]

        # creates a new head of the Snake upon movement to the right
        if snake_move == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)
        # creates a new head of the Snake upon movement to the left
        elif snake_move == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        # creates a new head of the Snake upon donwards movement
        elif snake_move == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])
        # creates a new head of the Snake upon upwards movement
        elif snake_move == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        
        # inserts a new head of the Snake, styles it to a diamond symbol
        snake.insert(0, new_head)
        new_window.addch(new_head[0], new_head[1], curses.ACS_DIAMOND)
        
        # gets rid of the last position of the Snake's tail
        tail_remove = snake.pop()
        new_window.addstr(tail_remove[0], tail_remove[1], " ")

        # continously refreshes the window to update the terminal screen
        new_window.refresh()
        

"""
Wrapper allows to restore the terminal to a sane state
if the application raises an error
"""
curses.wrapper(main)