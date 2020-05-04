import pygame
import pgzrun
from collections import namedtuple


Size = namedtuple("Size", "x y")
size = Size(600, 400)

def update():
    screen.clear()
    pygame.mouse.set_visible(True)
    x, y = pygame.mouse.get_pos()
    screen.draw.circle((x,y), 50, "yellow")
    
pgzrun.go()
