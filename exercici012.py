#Arxiu exercici012.py
import pygame
import sys
import utils
import random
from assets.svgmoji.emojis import get_emoji

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
PINK = (255, 130, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 012')

CELL_SIZE = 50
img_tree = get_emoji(pygame, "🌲", size=CELL_SIZE)
img_sman = get_emoji(pygame, "☃️", size=CELL_SIZE)
img_snow = get_emoji(pygame, "❄️", size=CELL_SIZE)
img_skater = get_emoji(pygame, "🏂", size=CELL_SIZE)
pos_jugador = {'fila': 0, 'columna': 0}
board = []

def main():
    is_looping = True
    
    init_board()

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global pos_jugador
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            i = pos_jugador['fila']
            j = pos_jugador['columna']
            if event.key == pygame.K_RIGHT:
                i += 1
            elif event.key == pygame.K_LEFT:
                i -= 1
            elif event.key == pygame.K_UP:
                j -= 1
            elif event.key == pygame.K_DOWN:
                j += 1

            # Comprobamos si el jugador puede ir a la casilla
            if is_skiable_cell(i, j):
                pos_jugador['fila'] = i
                pos_jugador['columna'] = j
    return True

def app_run():
    pass

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # Dibujamos tablero
    inici_board_x = CELL_SIZE
    inici_board_y = CELL_SIZE
    ample_board = len(board) * CELL_SIZE
    altura_board = len(board[0]) * CELL_SIZE
    pygame.draw.rect(screen, LIGHT_BLUE, (inici_board_x, inici_board_y, ample_board, altura_board))

    # Dibujamos emojis
    for i, fila in enumerate(board):
        for j, casella in enumerate(fila):

            pos_x = inici_board_x + CELL_SIZE * i
            pos_y = inici_board_y + CELL_SIZE * j
            pos = (pos_x, pos_y)
            if casella == 'T':
                screen.blit(img_tree, pos)
            elif casella == 'M':
                screen.blit(img_sman, pos)
            elif casella == 'S':
                screen.blit(img_snow, pos)

    # Dibujamos el personaje
    pos_x = inici_board_x + pos_jugador['fila'] * CELL_SIZE
    pos_y = inici_board_y + pos_jugador['columna'] * CELL_SIZE
    screen.blit(img_skater, (pos_x, pos_y))

    pygame.display.update()

def place_random_letter(letter, count):
    global board
    filas = len(board)
    columnas = len(board[0])
    counter = 0
    
    while counter < count:
        i = random.randint(0, filas - 1)
        j = random.randint(0, columnas - 1)
        if i != 0 and j != 0 and board[i][j] == "":
            board[i][j] = letter
            counter += 1

def init_board():
    global board
    # Creamos el tablero vacío
    board = []
    filas = 10
    columnas = 8
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("")
        board.append(fila)

    # Añadimos las letras al tablero
    place_random_letter('T', 9)
    place_random_letter('S', 3)
    place_random_letter('M', 3)

def is_skiable_cell(row, col):
    global board
    filas = len(board)
    columnas = len(board[0])

    casella_fora_tauler = (row not in range(filas)) or (col not in range(columnas))
    if casella_fora_tauler:
        return False
    arbre_o_ninot = board[row][col] in ['T','M']
    if arbre_o_ninot:
        return False
    return True

if __name__ == '__main__':
    main()