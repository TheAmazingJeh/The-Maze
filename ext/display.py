from operator import le
import pygame as PYG
import os
import time

class Display():
    def __init__(self):
        pass

    def construct_display(self,display_surface,level_data,images):
        """
        Current Display Surface , Level Data , image list -> Updated Display Surface (Object)
        """
        pos_X,pos_Y = 32,32
        texture_data = level_data["texture_data"]
        for line in texture_data:
            # input(f"1 {level_data}")
            # Looping LISTS in DICT level_data
            for num in texture_data[line]:
                match num:
                    case 0: display_surface.blit(self.return_image("floor",images),(pos_X,pos_Y))
                    case 1: display_surface.blit(self.return_image("brick",images),(pos_X,pos_Y))
                    case 2: display_surface.blit(self.return_image("brickCracked",images),(pos_X,pos_Y))
                    case _: display_surface.blit(self.return_image("missingImg",images),(pos_X,pos_Y))
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
        rescale_data = level_data["texture_data"]
        X_unit = 0
        Y_unit = 0
        for line in rescale_data:
            if len(rescale_data[line]) > X_unit:
                X_unit = len(rescale_data[line])
        Y_unit = len(rescale_data)
        return X_unit*32 + 64,Y_unit*32 + 64
            

    def rescale_tile(self,image_to_rescale):
        """
        Pygame Image -> Rescaled Pygame Image (Object)
        """
        return PYG.transform.scale(image_to_rescale, (32, 32))



if __name__ == "__main__":
    os.system("color 0c")
    input("""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ This is not the correct file to run. ┃
    ┃                                      ┃
    ┃         Please run main.py           ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
      
      Press enter to close...""")