#Arxiu exercici015.py
import pygame
import sys
import utils

WHITE = (255,255,255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 015')

def main():
    is_looping = True
    
    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

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

    columns = 21
    saturation = 1.0
    lightness = 0.5
    for column in range(columns):
        x = 50 + column * 25
        hue = (360 / columns) * column
        color = utils.hsl_to_rgb(hue, saturation, lightness)
        pygame.draw.rect(screen, color, (x, 200, 25, 25))

    pygame.display.update()

if __name__ == '__main__':
    main()