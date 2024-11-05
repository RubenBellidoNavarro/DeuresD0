#Arxiu exercici016.py
import pygame
import sys
import utils

WHITE = (255,255,255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 016')

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

    rows = 15
    columns = 21
    saturation = 1.0
    for row in range(0, rows):
        y = 50 + row * 25
        for column in range(0, columns):
            hue = (360 / columns) * column
            ligthness = (1 / rows) * row
            color = utils.hsl_to_rgb(hue, saturation, ligthness)
            x = 50 + column * 25
            pygame.draw.rect(screen, color, (x, y, 25, 25))

    pygame.display.update()

if __name__ == '__main__':
    main()