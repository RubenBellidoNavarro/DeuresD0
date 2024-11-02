#Arxiu exercici005.py
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

    #dibuixem espiral
    center_x, center_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
    increment = 15
    punts = []
    for i in range(26):
        if i == 0:
            punt = (center_x, center_y)
            punts.append(punt)
            continue

        modul = i % 4
        punt = list(punts[-1])
        if modul == 1:
            punt[0] += increment * i
        elif modul == 2:
            punt[1] -= increment * i
        elif modul == 3:
            punt[0] -= increment * i
        elif modul == 0:
            punt[1] += increment * i

        pygame.draw.line(screen, RED, punts[-1], punt, 5)

        punt = tuple(punt)
        punts.append(punt)

    pygame.display.update()

if __name__ == '__main__':
    main()