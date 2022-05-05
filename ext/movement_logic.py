import pygame as PYG
import os

class Movement():
    def __init__(self):    
        self.valid_keys = {
            "movement":{
                "up":PYG.K_w,
                "down":PYG.K_s,
                "left":PYG.K_a,
                "right":PYG.K_d,
            },
        }

    def collect_movement(self,keys_pressed):
        if len(keys_pressed) > 0:
            if keys_pressed[self.valid_keys["movement"]["up"]]:
                return (0,1)
            elif keys_pressed[self.valid_keys["movement"]["down"]]:
                return (0,-1)
            elif keys_pressed[self.valid_keys["movement"]["left"]]:
                return (-1,0)
            elif keys_pressed[self.valid_keys["movement"]["right"]]:
                return (1,0)
            else:
                return (0,0)

    def move_player(self,level_data,direction):
        
        new_player_locationXY = (0,0)
        new_player_location   = []
        detail_location   = []    # Buttons, switches ext.

        if direction is not None:
            # Do direction things
            pass
        return {
            "Ignore Event": False,
            "texture_data": level_data["texture_data"],
            "player_location": new_player_location,
            "PlayerXY": new_player_locationXY,
            "detail_location": detail_location
        }


if __name__ == "__main__":
    os.system("color 0c")
    input("""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ This is not the correct file to run. ┃
    ┃                                      ┃
    ┃         Please run main.py           ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
      
      Press enter to close...""")