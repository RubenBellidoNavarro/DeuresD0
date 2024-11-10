#Arxiu exercici022.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (165,42,42)
GREEN = (0, 255, 0)
BLUE  = (50, 120, 200)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 022')

mouse_inside = False
mouse_pos = {
    'x': -1,
    'y': -1
}
CELL_WIDTH = 25
CELL_HEIGHT = 50
N_CELLS = 22
heights = [5] * N_CELLS

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
    global mouse_pos
    mouse_inside = pygame.mouse.get_focused()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos['x'] = event.pos[0]
                mouse_pos['y'] = event.pos[1]
            else:
                mouse_pos['x'] = -1
                mouse_pos['y'] = -1
    return True

def app_run():
    mouse_en_casella = False
    x_min = 50
    x_max = x_min + CELL_WIDTH * N_CELLS
    y_min = 200
    y_max = y_min + CELL_HEIGHT
    if (mouse_pos['x'] in range(x_min, x_max)) and (mouse_pos['y'] in range (y_min, y_max)):
        mouse_en_casella = True

    for cnt in range(N_CELLS):
        if mouse_en_casella:
            cell_x = x_min + cnt * CELL_WIDTH + (CELL_WIDTH / 2)
            distance = abs(cell_x - mouse_pos["x"])

            max_distance = 200
            heights[cnt] = max(5, 45 - min(distance, max_distance) * (40 / max_distance))
        else:
            heights[cnt] = 5


def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # Dibujamos las casillas:
    for cnt in range(N_CELLS):
        x = 50 + cnt * CELL_WIDTH
        height = 5 + heights[cnt]
        y_min = 250 - height
        rect_values = (x, y_min, CELL_WIDTH, height)
        pygame.draw.rect(screen, BLACK, rect_values)
    
    pygame.display.update()

if __name__ == '__main__':
    main()