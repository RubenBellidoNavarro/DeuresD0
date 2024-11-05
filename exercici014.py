#Arxiu exercici014.py
import pygame
import sys
import utils

WHITE = (255,255,255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 014')

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

    pos = [50, 150]
    for counter in range(11):
        light = counter * (255 / 10)
        for i in range(4):
            color = [0,0,0]
            if i != 3:
                color[i] = light
            else:
                color = [light, light, light]
            pygame.draw.rect(screen, color, (pos[0], pos[1], 50, 50))
            pos[1] += 50
        pos[0] += 50
        pos[1] = 150

    pygame.display.update()

if __name__ == '__main__':
    main()