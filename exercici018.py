#Arxiu exercici018.py
import pygame
import sys
import utils
import math

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 018')

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
    saturation = 1.0
    lightness = 0.5
    punts_polygon = {'punt_radiPetit_lineaActual': 0, 'punt_radiPetit_lineaAnterior': 0, 'punt_radiGran_lineaAnterior': 0, 'punt_radiGran_lineaActual': 0,}

    for angle_deg in range(0, 361, 15):
        # 'hue' es un valor entre 0 y 360, y es linealmente proporcional al recorrido del bucle for
        hue = angle_deg
        color = utils.hsl_to_rgb(hue, saturation, lightness)

        angle_rad = (angle_deg / 360) * (2 * math.pi)
        punts_polygon['punt_radiPetit_lineaActual'] = {'x': center['x'] + math.cos(angle_rad) * radi_petit, 'y': center['y'] + math.sin(angle_rad) * radi_petit}
        punts_polygon['punt_radiGran_lineaActual'] = utils.point_on_circle(center, radi_gran, angle_deg)
        if angle_deg != 0:
            # Tenemos los puntos guardados en un diccionario de diccionarios, y queremos obtener un array de tuplas
            array_punts = list(map(lambda dict_punt : (dict_punt['x'], dict_punt['y']), punts_polygon.values()))
            pygame.draw.polygon(screen, color, array_punts)
        punts_polygon['punt_radiPetit_lineaAnterior'] = punts_polygon['punt_radiPetit_lineaActual']
        punts_polygon['punt_radiGran_lineaAnterior'] = punts_polygon['punt_radiGran_lineaActual']

    pygame.display.update()

if __name__ == '__main__':
    main()