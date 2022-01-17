import pygame as PYG
from ext.logger import Logger

class Movement():
    def __init__(self):
        log = Logger()
        log.log_init("Info","Initialization","Class","Logic")
        self.valid_keys = {
            "movement":{
                "num":{
                    "up":[1073741906,119],
                    "down":[1073741905,97],
                    "left":[1073741904,115],
                    "right":[1073741903,100],
                    },
                "keyvar":{
                    "up":[PYG.K_w],
                    "down":[PYG.K_s],
                    "left":[PYG.K_a],
                    "right":[PYG.K_d],
                },
            },
        }

    def collect_movement(self,key_pressed,key_pressed_value):
        print(key_pressed)
        return


        if len(key_pressed_value) > 0:
            if key_pressed in self.valid_keys["movement"]["num"]["up"] and key_pressed_value[PYG.K_w]:
                return (0,1)
            elif key_pressed in self.valid_keys["movement"]["num"]["down"]:
                return (0,-1)
            elif key_pressed in self.valid_keys["movement"]["num"]["left"]:
                return (-1,0)
            elif key_pressed in self.valid_keys["movement"]["num"]["right"]:
                return (1,0)
        return (0,0)

    def move_player(self,level_data,direction):
        
        if direction is not None:
            # Do direction things
            pass
        return {
            "Ignore Event": False,
            "level_data": level_data
        }