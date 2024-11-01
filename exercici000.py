#Arxiu exercici000.py
import utils
import pygame
import sys

# Definimos colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PINK = (255, 130, 203)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

#Iniciamos modulos pygame y creamos reloj
pygame.init()
clock = pygame.time.Clock()

#Creamos pantalla
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Exercici 000')

#Bucle de la aplicación
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

#Gestionamos eventos
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

#Hacemos cálculos
def app_run():
    pass

#Dibujamos en pantalla:
def app_draw():

    #Pintamos pantalla de blanco
    screen.fill(WHITE)

    #Dibujamos grid
    utils.draw_grid(pygame, screen, 50)
    #Dibujamos cuadrado rosa
    pygame.draw.rect(screen, PINK, (150, 200, 50, 50), 5)
    #Dibujamos triángulo verde
    pygame.draw.polygon(screen, GREEN, ((250,250),(275,200),(300,250)), 5)
    #Dibujamos cruz azul
    pygame.draw.line(screen, BLUE, (350,250), (400,200), 5)
    pygame.draw.line(screen, BLUE, (350,200), (400,250), 5)
    #Dibujamos circulo rojo
    pygame.draw.circle(screen, RED, (475, 225), 25, 5)

    #Actualizamos dibujo en pantalla
    pygame.display.update()

if __name__ == '__main__':
    main()