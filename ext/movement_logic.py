import pygame as PYG
from ext.logger import Logger

class Movement():
    def __init__(self):
        log = Logger()
        log.log_init("Info","Initialization","Class","Logic")
        
    def collect_movement(self,keys_pressed):
        if len(keys_pressed) > 0:
            if keys_pressed[PYG.K_UP] or keys_pressed[PYG.K_w]:
                return (1,0)
            elif keys_pressed[PYG.K_DOWN] or keys_pressed[PYG.K_s]:
                return (-1,0)
            elif keys_pressed[PYG.K_LEFT] or keys_pressed[PYG.K_a]:
                return (0,-1)
            elif keys_pressed[PYG.K_RIGHT]  or keys_pressed[PYG.K_d]:
                return (0,1)
            else:
                return None
        

    def move_player(self,level_data,direction):
        
        if direction is not None:
            print(direction)
        return {
            "Ignore Event": False,
            "level_data": level_data
        }