#Arxiu exercici008.py
import pygame
import sys
import utils

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
pygame.display.set_caption('Exercici 008')

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

    #dibuixem tauler
    colors = [(127, 184, 68), (240, 187, 64), (226, 137, 50), (202, 73, 65), (135, 65, 152), (75, 154, 217)]
    board = [
        [0, 1, 2, 3, 4, 5, 4, 3],
        [1, 2, 3, 4, 5, 4, 3, 2],
        [2, 3, 4, 5, 4, 3, 2, 1],
        [3, 4, 5, 4, 3, 2, 1, 0],
        [4, 5, 4, 3, 2, 1, 0, 1],
        [5, 4, 3, 2, 1, 0, 1, 2],
        [4, 3, 2, 1, 0, 1, 2, 3],
        [3, 2, 1, 0, 1, 2, 3, 4],
    ]
    mida_board = len(board)
    pos_x = 50
    pos_y = 50
    for fila in range(mida_board):
        for element in board[fila]:
            pygame.draw.rect(screen, colors[element], (pos_x, pos_y, 50, 50))
            pos_x += 50
        pos_x = 50
        pos_y += 50

    pygame.display.update()

if __name__ == '__main__':
    main()