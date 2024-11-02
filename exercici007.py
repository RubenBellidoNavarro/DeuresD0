#Arxiu exercici007.py
import pygame
import sys
import utils
import math

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

    #figuras
    colors = [(127, 184, 68), (240, 187, 64), (226, 137, 50), (202, 73, 65), (135, 65, 152), (75, 154, 217)]
    escala_grises = [0,0,0]
    pos_x = 50
    for q in range (0, len(colors)):
        color = colors[q]

        pygame.draw.rect(screen, color, (pos_x, 50, 50, 50))

        centre = [pos_x + 25, 175]
        pygame.draw.circle(screen, color, centre, 25, 2)

        centre[1] += 100
        draw_polygon(screen, escala_grises, centre, 25, 3)

        centre[1] += 100
        draw_polygon(screen, escala_grises, centre, 25, 5)

        pos_x += 100
        for i in range(3):
            escala_grises[i] += 25

    pygame.display.update()

def draw_polygon(screen, color, center, radius, num_vertices, angle_offset=(math.pi / 3)):
    points = [
        (
            center[0] + radius * math.cos(angle_offset + i * 2 * math.pi / num_vertices),
            center[1] + radius * math.sin(angle_offset + i * 2 * math.pi / num_vertices)
        )
        for i in range(num_vertices)
    ]
    pygame.draw.polygon(screen, color, points)

if __name__ == '__main__':
    main()