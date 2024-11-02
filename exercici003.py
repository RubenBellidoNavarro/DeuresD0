#Arxiu exercici003.py
import pygame
import sys
import utils
import os

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

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

    pygame.exit()
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

    #cercles blancs i vermells
    centre = (350,250)
    radi = 225
    color = RED
    for i in range(9):
        pygame.draw.circle(screen, color, centre, radi)
        radi -= 25
        if color == RED:
            color = WHITE
        elif color == WHITE:
            color = RED

    #cercles negres
    radi = 225
    for i in range(9):
        pygame.draw.circle(screen, BLACK, centre, radi, 5)
        radi -= 25

    pygame.display.update()

if __name__ == '__main__':
    main()