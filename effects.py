import pygame as PYG
from time import sleep
from logger import Logger

class Effect():
    def __init__(self):
        log = Logger()
        log.log_init("Info","Initilization","Class","Effects")
    
    def fade_to_black(self,display_surface):
        black_surface = PYG.Surface((display_surface.get_width(), display_surface.get_height()), flags= PYG.SRCALPHA)
        color = (255, 255, 255, 1)
        black_surface.fill(color)
        alpha_key = 1
        while alpha_key <= 255:
            display_surface.blit(black_surface, display_surface.get_rect())
            alpha_key = alpha_key + 1
            sleep(1)