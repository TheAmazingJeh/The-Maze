## The Maze - Main
from logger import Logger # Import Logger
log = Logger()            # Initialize Logger
log.LOGGER_INIT()
log.log_init("Info","Initilization","Library","os")
import os # Import os

## Set Environmental Variables
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_WINDOW_POS'] = "128,128"

## Import Libraries
log.log_init("Info","Initilization","Library","Pygame")
import pygame as PYG

## Import Custom Libraries
from display import Display
from movement_logic import Movement
from effects import Effect

## Game Window Data

def main():
############################################################# Create instances of  Classes
    display = Display()   # Create Instance of Display class
    move = Movement()
    effect = Effect()
############################################################# Create Variables / Objects for game setup
    #input()
    mainLoop = True          # Variable for main game loop
    clock = PYG.time.Clock() # Create Clock (FPS)
    NAME = "The MAZE"
    ICON = display.get_tile("brick")
    FPS = 10                 # FPS
    ALLOW_CLOSE = True       # Allow the [x] button to close the game
    keys_pressed = []        # List to handle pressed keys.
    direction = (0,0)        # Direction tuple
############################################################# Window Setup
         # Set start location for window
    PYG.init()                                         # Initialise Pygame
    display_surface = PYG.display.set_mode((100,100))  # Default screen size
    PYG.display.set_caption(NAME)                      # Set title / caption
    PYG.display.set_icon(ICON)

    col_list = {
        "WHITE" :(255,255,255),
        "BLACK" :(  0,  0,  0),
        "RED"   :(255,  0,  0),
        "YELLOW":(255,255,  0),
    }

    # TEMP ##################################### Creating dummy level data
    level_data = {
            "l1":[1,1,1,1,1,1,1,1,1,1,1,1],
            "l2":[1,3,0,0,2,1,2,2,0,1,1,1],
            "l3":[1,1,1,0,0,2,2,0,0,0,1,1],
            "l4":[1,1,1,1,1,1,1,1,1,1,1,1],
        }

    level_data2 = {
            "l1":[1,1,1,1,1,1,1,1,1,1,1,1],
            "l2":[1,3,0,0,2,1,2,2,0,1,1,1],
            "l3":[1,1,1,0,0,2,2,0,0,0,1,0],
            "l4":[1,1,1,1,1,1,1,1,1,1,1,1],
        }
    # TEMP #####################################

    levelXY = display.rescale_display(level_data)   # Get level x and y data, 
    display_surface = PYG.display.set_mode(levelXY) # Resize Display to fit Level (using the level_data var)
    
    images = {
        "floor":        display.get_tile("floor"),
        "brick":        display.get_tile("brick"),
        "brickCracked": display.get_tile("brickCracked"),
        "missingImg":   display.get_tile("missingImg"),
    }
    display.rescale_display(level_data)
    while mainLoop:        
        clock.tick(FPS)
############################################################# Handle Pygame events

        move_data = move.move_player(level_data,direction)

        if move_data["Ignore Event"] != True:
            for event in PYG.event.get() :
                direction = move.collect_movement(keys_pressed)
                if event.type == PYG.QUIT :           ## Pygame Quit event. (X button)
                    if ALLOW_CLOSE == True:           # Test variable
                        log.log_init("Event Log","PYG.QUIT","PYG Event","Pygame")
                        log.log_init("Info","Closing","Library","Pygame")
                        PYG.quit()                    # Close Pygame 
                        log.log_init("Info","Closing","","Python")
                        quit()                        # Close Python
                if event.type == PYG.MOUSEBUTTONDOWN: ## Pygame Mouse Click event.
                    log.log_init("Event Log","PYG.MOUSEBUTTONDOWN","PYG Event","Pygame")
                    level_data=level_data2
                    #effect.fade_to_black(display_surface)                              # Click Detection

            keys_pressed = PYG.key.get_pressed()

        display_surface = display.construct_display(display_surface,level_data,images)
        PYG.display.update()

# PYG.display.set_icon() - needs pygame.surface

if __name__ == "__main__":
    main()
