# Arcade Terminal
Developed by **Dorian Wolarz**, a Code Institute Student

*Arcade Terminal is a Python game which runs in the Code Institute mock terminal on the Heroku webpage. Users can play the classic game of Snake, where they maneuver the end of a growing line in order to collect and consume apples, all while avoiding game-ending collisions.*

![Image of My Website on Multiple Devices](IMAGE LINK)

## Contents
1. [How to Play](#how-to-play)
2. [Features](#features)
3. [Data Model](#data-model)
4. [Planning](#planning)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

## How to Play

Arcade Terminal is based on the classic game of Snake, which originated in 1976 in the arcade game *'Blockade'*.

The player uses his arrow keys to move the titular Snake around the board.

If the Snake finds an apple, it eats it and grows larger by one segment.

The game ends when the Snake collides with the edge of the terminal screen or with its own tail.

The goal of the game is to make the Snake as large as possible before that happens.

## Features

This application consists of X features

### Main Menu
* Activated on application start
* Fits into the terminal screen
* Allows the user to navigate the application's interactive options
<br>
<img src="docs/features/f-mainmenu.png" alt="Main Menu" title="Main Menu Screen">

### Play Arcade Terminal
* Allows the player to activate the Snake game on correct input
* Fits into the terminal screen
<br>
<img src="docs/features/f-mm1.png" alt="Play Arcade Terminal" title="Play the Game Screen">

### How to Play
* Informs the user of the rules of gameplay
* Fits into the terminal screen
<br>
<img src="docs/features/f-mm2.png" alt="How to Play" title="How to Play Message">

### Quit the Application
* Allows the user to manually quit the application's terminal screen
* Fits into the terminal screen
<br>
<img src="docs/features/f-mm3.png" alt="Quit the App" title="Quit the App Message">

### Incorrect Key Input
* Informs the user of incorrect key input
* Reloads the main menu upon incorrect input so that user can see his options and try again
* Fits into the terminal screen
<br>
<img src="docs/features/f-mm4.png" alt="Incorrect Input" title="Incorrect Input Message">

### Snake
* Allows the player to move across the terminal and interact with its environment
* Can grow in size depending on the number of apples eaten
* Activates collisions with the terminal border and its own tail
<br>
<img src="docs/features/f-snake.png" alt="Snake" title="Snake">

### Apple
* Can be interacted with and consumed by the Snake
* Spawns in random areas within the terminal screen
<br>
<img src="docs/features/f-apple.png" alt="Apple" title="Apple">

### Score
* Located in the center-top of the terminal border for clear visibility
* Keeps track of current player score and increments by one after each apple eaten
<br>
<img src="docs/features/f-score.png" alt="Score" title="Score">

### Wall Collision
* Listens for the collision of the Snake
* Ends the game upon collision with wall and allows the player to exit the terminal by pressing any key
<br>
<img src="docs/features/f-go1.png" alt="Wall Collision" title="Wall Collision">

### Self Collision
* Listens for the collision of the Snake
* Ends the game upon collision with self and allows the player to exit the terminal by pressing any key
<br>
<img src="docs/features/f-go2.png" alt="Self Collision" title="Self Collision">

## Data Model

## Planning

## Technologies Used

### Languages

* Python 3

### Tools and Websites

* Git
* GitHub
* GitPod

## Testing

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

You can fork the repository by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner

After the repository is forked, you can deploy it by following these steps:

1. Create a new Heroku app
2. Set the buildbacks to *Python* and *NodeJS*, in that exact order
3. Link the Heroku app to the repository you have forked
4. Click on *Deploy*

## Credits

* *Code Institute* for the Python Essentials template on GitHub
* *Code Institute* for the deployment terminal on Heroku
* [Documentation for *curses* library](https://docs.python.org/3/library/curses.html#module-curses)
* [Documentation for *random* library](https://www.w3schools.com/python/module_random.asp)
* [*ASCII Art Alignment* by blhsing](https://stackoverflow.com/questions/51606897/ascii-characters-text-align)
* [*Text to ASCII Art* website by patorjk](https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Ogre&t=Arcade%20Terminal)
* [TUTORIAL and some Code Help: *Snake Game for Terminal* by Indian Pythonista](https://www.youtube.com/watch?v=BvbqI6eDh0c)
* [TUTORIAL: *Snake in the Powershell* by Clear Code](https://www.youtube.com/watch?v=lAIawk2IVIM)
* [TUTORIAL: *Snake Game in Python* by Patrick Loeber](https://www.youtube.com/watch?v=M_npdRYD4K0)
* [TUTORIAL: *Python Snake Game* by Mision Codigo](https://www.youtube.com/watch?v=_IKIkRMfZJA)