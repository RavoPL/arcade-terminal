"""
Imports the 'random' built-in Python library which can be used to return
a random number or value
Imports the 'curses' built-in Python library which can be used to create
a terminal-independent screen-painting and key-handling facility
"""
import random
import curses

"""
Function that creates an interactive main menu screen and its options
ASCII Art center code by blhsing
"""


def main_menu():
    title = '''      _                     _        _____                    _             _ 
      /_\  _ __ ___ __ _  __| | ___  /__   \___ _ __ _ __ ___ (_)_ __   __ _| |
    // _\\| '__/ __/ _` |/ _` |/ _ \   / /\/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
    /  _  \ | | (_| (_| | (_| |  __/  / / |  __/ |  | | | | | | | | | | (_| | |
    \_/ \_/_|  \___\__,_|\__,_|\___|  \/   \___|_|  |_| |_| |_|_|_| |_|\__,_|_|'''
    print('\n'.join(l.center(80) for l in title.splitlines()))
    print("Welcome to Arcade Terminal!")
    print("[1] Play Arcade Terminal")
    print("[2] How to Play")
    print("[3] Quit the Application")


main_menu()
choice = int(input("Enter your choice here: "))

while choice != 1:
    if choice == 2:
        # lists the rules of Arcade Terminal gameplay
        print("Use the arrow keys to move the Snake.")
        print("Collect red apples to grow and increase the Score.")
        print("The game is over if you collide with the wall or your tail.")
    elif choice == 3:
        # quits the Arcade Terminal application
        print("Thank you for playing Arcade Terminal!")
        exit()
    else:
        # informs the user of incorrect input and allows him to try again
        print("You've pressed the wrong number!")
        main_menu()
        choice = int(input("Enter your choice here: "))
    
    main_menu()
    choice = int(input("Enter your choice here: "))

"""
Function that builds a 'current score' display in the center of the screen
"""


def print_score(new_window, score):
    # returns a tuple of the max height and width of the screen
    sh, sw = new_window.getmaxyx()
    # sets initial score to 0 and centers the text above the terminal
    score_text = "Score: {}".format(score)
    new_window.addstr(0, (sw // 2) - len(score_text) // 2, score_text)


"""
Function that organically creates apples within the terminal box
"""


def create_apples(new_window, snake):
    # returns a tuple of the max height and width of the screen
    sh, sw = new_window.getmaxyx()
    # when there is no apple present it creates a new one within the border
    apple = None
    while apple is None:
        apple = (random.randint(1, sh-2), random.randint(1, sw-2))
        # if the apple is eaten, it removes an apple from the screen
        if apple in snake:
            apple = None
    return apple


"""
List of available player directions for the Snake's movement in the terminal
and
Dictionary that prevents the player from pressing opposite keys and harming the Snake
"""


directional_keys = [
    curses.KEY_RIGHT,
    curses.KEY_LEFT,
    curses.KEY_DOWN,
    curses.KEY_UP
]
opposite_keys = {
    curses.KEY_RIGHT: curses.KEY_LEFT,
    curses.KEY_LEFT: curses.KEY_RIGHT,
    curses.KEY_DOWN: curses.KEY_UP,
    curses.KEY_UP: curses.KEY_DOWN
}

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

    # sets and initializes the curses color pairs if terminal supports color
    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # creates the initial apple centered in the middle of the screen, styles it to a degree symbol
    apple = create_apples(new_window, snake)
    new_window.addch(apple[0], apple[1], curses.ACS_DEGREE, curses.color_pair(1))
    
    # initializes the score display in the terminal
    score = 0
    print_score(new_window, score)
    
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
            game_over = "GAME OVER! You collided with the wall! Press any key to exit"
            new_window.addstr(int(sh//2), int(sw//2) - len(game_over)//2, game_over)
            new_window.nodelay(0)
            new_window.getch()
            quit()
        # displays game over screen if Snake's head collides with any other body part
        if snake[0] in snake[1:]:
            ate_self = "GAME OVER! You ate your own tail! Press any key to exit"
            new_window.addstr(int(sh//2), int(sw//2) - len(ate_self)//2, ate_self)
            new_window.nodelay(0)
            new_window.getch()
            quit()

        # listens for the 'Q' key press so the user can quit the terminal screen
        key = new_window.getch()
        if key == ord("q"):
            break

        """
        some snake movement foundations by Indian Pythonista, with changes made by me
        """
        # listens for key input on arrow keys, changes movement of Snake
        # prevents opposite key movement depending on which key is pressed
        if key in directional_keys and key != opposite_keys[snake_move]:
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
        new_window.addch(new_head[0], new_head[1], curses.ACS_DIAMOND, curses.color_pair(2))

        # checks if the Snake ate the apple, removes it and creates a new one if eaten
        # increments by one point if apple is consumed
        # removes the tail of the Snake for every movement, overwritten by eating apples
        if snake[0] == apple:
            apple = create_apples(new_window, snake)
            new_window.addch(apple[0], apple[1], curses.ACS_DEGREE, curses.color_pair(1))
            score += 1
            print_score(new_window, score)
        else:
            tail_remove = snake.pop()
            new_window.addstr(tail_remove[0], tail_remove[1], " ")

        # continously refreshes the window to update the terminal screen
        new_window.refresh()

"""
Wrapper allows to restore the terminal to a sane state
if the application raises an error
"""
curses.wrapper(main)