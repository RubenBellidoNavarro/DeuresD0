#Arxiu exercici023.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
BROWN = (165, 42, 42)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169) 
ORANGE = (255, 165, 0)
GOLD = (255, 215, 0)
RED = (255, 69, 0) 

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 023')

sun = {
    "pos": (0, 0),
    "radius": 20
}
planets = {
    "Mercury": { "distance": 58,  "speed": 47.87, "radius": 3.80, "color": GRAY, "angle": 0, "pos": (0, 0) },
    "Venus":   { "distance": 108, "speed": 35.02, "radius": 9.50, "color": GOLD, "angle": 0, "pos": (0, 0) },
    "Earth":   { "distance": 150, "speed": 29.78, "radius": 10.0, "color": BLUE, "angle": 0, "pos": (0, 0) },
    "Mars":    { "distance": 228, "speed": 24.07, "radius": 5.30, "color": RED,  "angle": 0, "pos": (0, 0) },
}

font = pygame.font.SysFont('Arial', 10)

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
    global sun, planets
    sun["pos"] = (int(screen.get_width() / 2), int(screen.get_height() / 2)) 
    center = {'x': sun['pos'][0], 'y': sun['pos'][1]}
    delta_time = clock.get_time() / 1000
    for nom_planeta in planets:
        planets[nom_planeta]['angle'] += planets[nom_planeta]['speed'] * delta_time
        coordenades_planet = utils.point_on_circle(center, planets[nom_planeta]['distance'], planets[nom_planeta]['angle'])
        planets[nom_planeta]['pos'] = (coordenades_planet['x'], coordenades_planet['y'])

def app_draw():
    screen.fill(BLACK)
    utils.draw_grid(pygame, screen, 50)

    # Dibujamos el sol
    pygame.draw.circle(screen, YELLOW, sun["pos"], sun["radius"])
    for nom_planeta in planets:
        # El cercle de la òrbita de color "GRAY = (169, 169, 169)"
        pygame.draw.circle(screen, GRAY, sun['pos'], planets[nom_planeta]['distance'], 1)
        # Cada planeta a la seva posició
        pygame.draw.circle(screen, planets[nom_planeta]['color'], planets[nom_planeta]['pos'], planets[nom_planeta]['radius'])
        # El nom del planeta
        label = font.render(nom_planeta, True, GRAY)
        label_rect = label.get_rect()
        label_rect.midleft = (planets[nom_planeta]["pos"][0] + planets[nom_planeta]["radius"] + 5, planets[nom_planeta]["pos"][1]) 
        screen.blit(label, label_rect)
    
    pygame.display.update()

if __name__ == '__main__':
    main()