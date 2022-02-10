import os

from time import sleep

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class Effect():
    def __init__(self):
        pass
    
    def fade_to_black(self,display_surface):
        black_surface = PYG.Surface((display_surface.get_width(), display_surface.get_height()), flags= PYG.SRCALPHA)
        color = (255, 255, 255, 1)
        black_surface.fill(color)
        alpha_key = 1
        while alpha_key <= 255:
            display_surface.blit(black_surface, display_surface.get_rect())
            alpha_key = alpha_key + 1
            sleep(1)



#You create a surface called black_surface, but you fill it with white. Fill it with black (eg. (0, 0, 0, 1)) and may work, but there's another problem:
#When you call display.flip() inside a loop where you change the screen surface, the display may not actually update if you don't let pygame handle events (e.g. by calling pygame.event.get()), depending on your OS. Also, while your loop runs, you can't handle events manually, e.g. the QUIT event. So while your screen fades to black, you can't quit your game.
#Generally, you should only have one main loop and not call blocking functions like pygame.time.sleep, but there are exceptions, of course).
#Here's simple Sprite-based example:

# https://stackoverflow.com/questions/54881269/pygame-fade-to-black-function

import pygame

class Fade(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
        self.alpha = 0
        self.direction = 1

    def update(self, events):
        print(self.alpha)
        self.image.fill((0, 0, 0, self.alpha))
        self.alpha += self.direction*10

        #if self.alpha > 255:
        #    self.alpha = 255
        #if self.alpha < -255:
        #    self.alpha = -255

        if self.alpha > 255 or self.alpha < 0:
            self.direction *= -1
            self.alpha += self.direction*10

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    sprites = pygame.sprite.Group(Fade())
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        sprites.update(events)
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, pygame.Color('dodgerblue'), (100, 100, 100, 100))
        sprites.draw(screen)
        pygame.display.update()
        clock.tick(5)

#main()