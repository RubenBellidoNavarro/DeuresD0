#Arxiu exercici010.py
#Arxiu exercici009.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 
GOLD = (255, 215, 0)
NAVY = (0, 0, 128)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 009')

def main():
    is_looping = True

    global rectangles, es_punt, mouse_pos
    rectangles = [
        { "rect": { "x": 50, "y": 100, "width": 250, "height": 50 }, "color": RED },
        { "rect": { "x": 50, "y": 200, "width": 100, "height": 200 }, "color": GOLD },
        { "rect": { "x": 200, "y": 200, "width": 100, "height": 100 }, "color": BLUE },
        { "rect": { "x": 200, "y": 350, "width": 400, "height": 50 }, "color": PURPLE },
        { "rect": { "x": 350, "y": 100, "width": 50, "height": 200 }, "color": ORANGE },
        { "rect": { "x": 450, "y": 100, "width": 150, "height": 100 }, "color": GREEN },
        { "rect": { "x": 450, "y": 250, "width": 150, "height": 50 }, "color": NAVY }
    ]
    
    es_punt = []
    for e in rectangles:
        es_punt.append(False)

    mouse_pos = {'x':-1, 'y':-1}

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

    pygame.quit()
    sys.exit()

def app_events():
    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos['x'] = event.pos[0]
                mouse_pos['y'] = event.pos[1]
            else:
                mouse_pos['x'] = -1
                mouse_pos['y'] = -1
    return True

def app_run():
    for index, rectangle in enumerate(rectangles):
        if utils.is_point_in_rect(mouse_pos, rectangle['rect']):
            es_punt[index] = True
        else:
            es_punt[index] = False

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    #dibuixem rectangles
    for index, ratoli_al_rect in enumerate(es_punt):
        rectangle_dict = rectangles[index]
        mesures = (rectangle_dict['rect']['x'], rectangle_dict['rect']['y'], rectangle_dict['rect']['width'], rectangle_dict['rect']['height'])
        if ratoli_al_rect:
            color = rectangle_dict['color']
            pygame.draw.rect(screen, color, mesures)
        pygame.draw.rect(screen, BLACK, mesures, 5)

    pygame.display.update()

if __name__ == '__main__':
    main()