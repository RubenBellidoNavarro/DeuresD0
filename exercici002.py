#Arxiu exercici002.py
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

    #shinnosuke
    path_shinnosuke = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shinnosuke.png")
    im_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
    im_shinnosuke = utils.scale_image(pygame, im_shinnosuke, target_width=100)
    screen.blit(im_shinnosuke, (330,160))

    #shiro
    path_shiro = os.path.join(os.path.dirname(__file__), './assets/exercici002/shiro.png')
    im_shiro = pygame.image.load(path_shiro).convert_alpha()
    im_shiro = utils.scale_image(pygame, im_shiro, target_width=75)
    screen.blit(im_shiro, (225,210))

    pygame.display.update()

if __name__ == '__main__':
    main()