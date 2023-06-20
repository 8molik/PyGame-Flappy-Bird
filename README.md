# PyGame-Flappy-Bird
# Project Description
Flappy Bird is a popular side-scrolling mobile game where the player controls a bird, attempting to navigate it through a series of pipes without colliding with them. The objective is to achieve the highest score possible by successfully maneuvering the bird through the gaps between the pipes.

## Gameplay
Upon starting the game, the player is presented with the start screen. In order to start playing, and continue to jump the player needs to press 'space'. To restart the game
it is necessary to click restart button with mouse.

## Complilation
To compile the project you need to write 'python main.py' in the game folder. Although you can run .exe file.

# Class & Methods Description
## Diagram
![image](https://github.com/8molik/PyGame-Flappy-Bird/assets/74592649/01eca676-6d8b-44f3-9246-e475eb97fe97)
## Class `GameObject` (abstract class representing game objects)
### Methods:
- `__init__()`: Initializes the game object.
- `display()`: Displays the game object on the screen.
- `get_rect()`: Returns the rectangular area occupied by the game object.

## Class `Background` (background)
### Methods:
- `__init__()`: Initializes the background.
- `display()`: Displays the background on the screen.
- `get_rect()`: Returns the rectangular area occupied by the background.

## Class `Base` (base of the screen)
### Methods:
- `__init__()`: Initializes the base.
- `display()`: Displays the base on the screen.
- `get_rect()`: Returns the rectangular area occupied by the base.

## Class `Bird` (bird/player)
### Methods:
- `__init__()`: Initializes the bird.
- `jump()`: Makes the bird jump.
- `update()`: Updates the position of the bird.
- `display()`: Displays the bird on the screen.
- `get_rect()`: Returns the rectangular area occupied by the bird.

## Class `Pipe` (pipe obstacle)
### Methods:
- `__init__()`: Initializes the pipe.
- `display()`: Displays the pipe on the screen.
- `move()`: Moves the pipe.
- `get_rect()`: Returns the rectangular area occupied by the pipe.

## Class `Sound` (sound)
### Methods:
- `__init__()`: Initializes the sound.
- `play_sound()`: Plays the sound.

## Class `Score` (score)
### Methods:
- `__init__()`: Initializes the score.
- `update_score()`: Updates the score.
- `generate_number()`: Generates the score as numbers.
- `display_score()`: Displays the score on the screen.

## Class `Menu` (start and end screens)
### Methods:
- `__init__()`: Initializes the menu.
- `display_start()`: Displays the start screen.
- `display_end()`: Displays the end screen.

## Class `Main` (main game logic)
### Methods:
- `__init__()`: Initializes the main game.
- `generate_pipes()`: Generates the pipes.
- `handle_hits()`: Handles collisions with pipes and the ground.
- `display()`: Displays the game on the screen.
- `handle_pipes()`: Handles the movement and generation of pipes.
- `main()`: Main game loop.
