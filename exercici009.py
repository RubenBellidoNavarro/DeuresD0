#Arxiu exercici009.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (50,120,200)
PINK = (255, 130, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 009')

def main():
    is_looping = True

    global dades, ARIAL_20, ARIAL_16
    dades = [ 
            {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
            {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
            {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
            {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
            {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
            {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'}
            ]
    ARIAL_20 = pygame.font.SysFont('Arial', 20)
    ARIAL_16 = pygame.font.SysFont('Arial', 16)

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

    #dibuixem taula
    altura_fila = 25
    posicio_inicial = [150,100]
    altura_taula = altura_fila * len(dades)
    ample_taula = 200
    gruix_linea_separadora = 3

    pygame.draw.rect(screen, WHITE, (posicio_inicial[0], posicio_inicial[1], ample_taula, altura_taula))

    for line in dades:
        posicio_final_linea = [posicio_inicial[0] + ample_taula, posicio_inicial[1]]
        pygame.draw.line(screen, BLACK, posicio_inicial, posicio_final_linea, gruix_linea_separadora)

        posicio_nom = [posicio_inicial[0] + 5, posicio_inicial[1] + 2]
        text_nom = ARIAL_20.render(line['nom'], True, BLACK)
        screen.blit(text_nom, posicio_nom)

        posicio_any = [posicio_nom[0] + 100, posicio_nom[1]]
        text_any = ARIAL_16.render(str(line['any']), True, BLUE)
        screen.blit(text_any, posicio_any)

        posicio_especie = [posicio_nom[0] + 150, posicio_nom[1]]
        text_especie = ARIAL_16.render(line['especie'], True, BLUE)
        screen.blit(text_especie, posicio_especie)

        posicio_inicial[1] += altura_fila

        # si es el último elemento, añade la linea final
        if line is dades[-1]:
            posicio_final_linea = [posicio_inicial[0] + ample_taula, posicio_inicial[1]]
            pygame.draw.line(screen, BLACK, posicio_inicial, posicio_final_linea, gruix_linea_separadora)

    pygame.display.update()

if __name__ == '__main__':
    main()