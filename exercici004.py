#Arxiu exercici004.py
import pygame
import sys
import utils
import os
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PINK = (255, 130, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 002')

def main():
    is_looping = True

    #definim punts
    global punts
    punts = []
    for i in range(10):
        rand_x = random.randint(0,640)
        rand_y = random.randint(0,480)
        punts.append((rand_x,rand_y))

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

    pygame.quit()
    sys.exit()

def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True

def app_run():
    pass

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    #dibuixem punts
    pygame.draw.polygon(screen, BLACK, punts, 5)

    pygame.display.update()

if __name__ == '__main__':
    main()