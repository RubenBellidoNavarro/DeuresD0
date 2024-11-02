#Arxiu exercici006.py
import pygame
import sys
import utils
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PINK = (255, 130, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (200, 200, 200)

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

    #dibuixem tauler
    punt_x = 50
    punt_y = 50
    for fila in range(8):
        for element in range(8):

            if fila % 2 == 0:
                if element % 2 == 0:
                    color = GREY
                else:
                    color = BLACK
            else:
                if element % 2 == 0:
                    color = BLACK
                else:
                    color = GREY

            pygame.draw.rect(screen, color, (punt_x, punt_y, 50, 50))
            punt_x += 50

        punt_x = 50
        punt_y += 50


    pygame.display.update()

if __name__ == '__main__':
    main()