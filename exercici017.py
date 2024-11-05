#Arxiu exercici017.py
import pygame
import sys
import utils
import math

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 017')

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

    center = {'x':300, 'y':250}
    radi_petit = 25
    radi_gran = 150
    for angle in range(0, 361, 15):
        # Pasar ángulo a radianes
        angle = (angle / 360) * (2 * math.pi)
        # Calcular componentes x e y del punto por trigonometría
        punt_radi_petit = {'x':math.cos(angle) * radi_petit, 'y':math.sin(angle) * radi_petit}
        #punt_radi_gran = utils.point_on_circle(center, radi_gran, angle)
        #pygame.draw.line(screen, BLACK, tuple(punt_radi_petit.values()), tuple(punt_radi_gran.values()), 5)

    pygame.display.update()

if __name__ == '__main__':
    main()