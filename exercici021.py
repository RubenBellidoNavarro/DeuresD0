#Arxiu exercici021.py
import pygame
import sys
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (165,42,42)
GREEN = (0, 255, 0)
BLUE  = (50, 120, 200)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 021')

board = {
    "position": { 
        "x": 50, 
        "y": 50 
    },
    "size": { 
        "rows": 15, 
        "cols": 10 
    },
    "cell_size": 25
}

mouse_pos = {
    "x": -1,
    "y": -1
}

font = pygame.font.SysFont('Arial', 20)

def main():
    is_looping = True

    # Generamos graella con números aleatorios entre 0 y 9
    global graella
    graella = []
    n_rows = board['size']['rows']
    n_cols = board['size']['cols']
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            n = random.randint(0, 9)
            row.append(n)
        graella.append(row)
    
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
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos['x'] = event.pos[0]
                mouse_pos['y'] = event.pos[1]
            else:
                mouse_pos['x'] = -1
                mouse_pos['y'] = -1
    return True

def app_run():
    pass

def app_draw():
    screen.fill(WHITE)

    # Si el ratón está sobre un número (celda), dibujamos un rectángulo en todos los números iguales
    celda = cell_from_point(mouse_pos, board)
    if tuple(celda.values()) != (-1, -1):
        n = get_cell_value(celda)
        n_rows = board['size']['rows']
        n_cols = board['size']['cols']
        for i in range(n_rows):
            for j in range(n_cols):
                if graella[i][j] == n:
                    celda = {'i': i, 'j': j}
                    pos_rect = point_from_cell(celda, board)
                    rect_values = (pos_rect['x'], pos_rect['y'], board['cell_size'], board['cell_size'])
                    pygame.draw.rect(screen, YELLOW, rect_values)

    # Dibujamos el tablero
    draw_board(board)

    # Dibujamos números
    draw_board_values()
    
    pygame.display.update()

def draw_board(board):
    x = board['position']['x']
    y = board['position']['y']
    n_rows = board['size']['rows']
    n_cols = board['size']['cols']

    for row in range(n_rows):
        for column in range(n_cols):
            rect_values = (x, y, board['cell_size'], board['cell_size'])
            pygame.draw.rect(screen, BLACK, rect_values, 1)
            x += board['cell_size']
        x = board['position']['x']
        y += board['cell_size']
    
def cell_from_point(point, board):
    x = board['position']['x']
    y = board['position']['y']
    n_rows = board['size']['rows']
    n_cols = board['size']['cols']

    for i, row in enumerate(range(n_rows)):
        for j, col in enumerate(range(n_cols)):
            x_en_rang = point['x'] in range(x, x + board['cell_size'])
            y_en_rang = point['y'] in range(y, y + board['cell_size'])
            if x_en_rang and y_en_rang:
                return {'i': i, 'j': j}
            x += board['cell_size']
        x = board['position']['x']
        y += board['cell_size']
    return {'i': -1, 'j': -1}

def point_from_cell(cell, board):
    x_inicial = board['position']['x']
    y_inicial = board['position']['y']
    n_rows = board['size']['rows']
    n_cols = board['size']['cols']

    for i, row in enumerate(range(n_rows)):
        for j, col in enumerate(range(n_cols)):
            if i == cell['i'] and j == cell['j']:
                x = x_inicial + j * board['cell_size']
                y = y_inicial + i * board['cell_size']
                return {'x': x, 'y': y}
    return {'x': -1, 'y': -1}

def get_cell_value(cell):
    i = cell['i']
    j = cell['j']
    return graella[i][j]

def draw_board_values():
    x = board['position']['x'] + 7
    y = board['position']['y']
    n_rows = board['size']['rows']
    n_cols = board['size']['cols']

    for i in range(n_rows):
        for j in range(n_cols):
            n = graella[i][j]
            n_text = font.render(str(n), True, BLACK)
            screen.blit(n_text, (x, y))
            x += board['cell_size']
        x = board['position']['x'] + 7
        y += board['cell_size']
        

if __name__ == '__main__':
    main()