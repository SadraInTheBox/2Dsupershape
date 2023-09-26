import pygame as pg
from pygame import QUIT
from .shape import SuperShape

def run():
    pg.init()

    window = pg.display.set_mode((700,700))
    pg.display.set_caption("super shapes")

    running = True

    shape = SuperShape(window)
    while running:
        window.fill((51,51,51))

        shape.draw()
        
        for event in pg.event.get():
            if event.type == QUIT:running = False

        pg.display.flip()