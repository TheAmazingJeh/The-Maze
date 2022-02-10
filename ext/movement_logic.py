import pygame as PYG
from ext.logger import Logger

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
        
        player_locationXY = (0,0)
        player_location   = []
        detail_location   = []    # Buttons ext.

        if direction is not None:
            # Do direction things
            pass
        return {
            "Ignore Event": False,
            "level_data": level_data,
            "player_location": player_location,
            "PlayerXY": player_locationXY,
            "details": detail_location
        }