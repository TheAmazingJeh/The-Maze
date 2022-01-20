import pygame as PYG
import os
import time
from ext.logger import Logger

class Display():
    def __init__(self):
        log = Logger()
        log.log_init("Info","Initialization","Class","Display")

    def construct_display(self,display_surface,level_data,images):
        """
        Current Display Surface , Level Data , image list -> Updated Display Surface (Object)
        """
        pos_X,pos_Y = 32,32

        associated_strings = [
            "floor",         # Default Floor Tile
            "brick",        # Default Brick Tile
            "brickCracked" # Default Cracked Bricks Tile
        ]

        for line in level_data:
            # input(f"1 {level_data}")
            # Looping LISTS in DICT level_data
            for num in level_data[line]:
                if num == 0:
                    display_surface.blit(self.return_image("floor",images),(pos_X,pos_Y))
                elif num == 1:
                    display_surface.blit(self.return_image("brick",images),(pos_X,pos_Y))
                elif num == 2:
                    display_surface.blit(self.return_image("brickCracked",images),(pos_X,pos_Y))

                else:
                    display_surface.blit(self.return_image("missingImg",images),(pos_X,pos_Y))
                pos_X += 32 # Move 32 px right

            pos_X = 32      # Move 32 px right
            pos_Y += 32     # Move 32 px down

        return display_surface
        
    def get_tile(self,name):
        """
        File Name -> Pygame Image Object (Object) (Tile)
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        reqImg = f"{dir_path}\\Assets\\image\\tile\\{name}.png"
        #input(reqImg)
        if os.path.exists(reqImg):
            return self.rescale_tile(PYG.image.load(reqImg))
        else:
            return self.rescale_tile(PYG.image.load(f"{dir_path}\\Assets\\image\\tile\\missingImg.png"))

    def get_sprite(self,name):
        """
        File Name -> Pygame Image Object (Object) (Sprite)
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        reqImg = f"{dir_path}\\Assets\\image\\sprite\\{name}.png"
        #input(reqImg)
        if os.path.exists(reqImg):
            return self.rescale_tile(PYG.image.load(reqImg))
        else:
            return self.rescale_tile(PYG.image.load(f"{dir_path}\\Assets\\image\\sprite\\missingImg.png"))

    def return_image(self,name,images):
        """
        File Name , Image List -> Image Name (String)
        """
        return images[name]

    def rescale_display(self,level_data):
        """
        Level Data -> Display X & Y (Tuple)
        """
        X_unit = 0
        Y_unit = 0
        for line in level_data:
            if len(level_data[line]) > X_unit:
                X_unit = len(level_data[line])
        Y_unit = len(level_data)
        return X_unit*32 + 64,Y_unit*32 + 64
            

    def rescale_tile(self,image_to_rescale):
        """
        Pygame Image -> Rescaled Pygame Image (Object)
        """
        return PYG.transform.scale(image_to_rescale, (32, 32))



if __name__ == "__main__":
    print(">>> Directly ran\n>>> Entering Debug mode")
    #input(">>> What do you want to do?\n>>>  ")
    os.environ['SDL_VIDEO_WINDOW_POS'] = "128,128"
    PYG.init()
    display = Display()   # Create Instance of Display class
    white = (255, 255, 255) # White Colour
    X,Y = 1024,512   # XY display size
    level_data = {
            "l1":[2,1,1,2,1,1,2,2,0,0,2,1],
            "l2":[1,1,1,2,0,0,0,2,0,1,2,1],
        }

    xy = display.rescale_display(level_data)
    display_surface = PYG.display.set_mode((100,100))
    display_surface = PYG.display.set_mode(xy) # Create Display
    
    # display_surface.set_mode((X, Y )) # Resize Display
    PYG.display.set_caption('Class Test [display]')    # Set Title / Caption

    images = {
        "floor":        display.get_image("floor"),
        "brick":        display.get_image("brick"),
        "brickCracked": display.get_image("brickCracked"),
        "missingImg":   display.get_image("missingImg"),
    }
    while True :
        
        #display_surface.set_mode(display.rescale_display(level_data))
        
        
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in PYG.event.get() :
            # if event object type is QUIT
            if event.type == PYG.QUIT :
                # deactivates the pygame library
                PYG.quit()
                # quit the program.
                quit()
            # Draws the surface object to the display. 
        display.rescale_display(level_data)
        display_surface = display.construct_display(display_surface,level_data,images)
        PYG.display.update() 
            
             
    
