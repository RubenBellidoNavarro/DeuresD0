#Arxiu exercici024.py
import pygame
import sys
import utils
from datetime import datetime

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
RED = (255, 69, 0) 

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 024')

time = { 
    "hours": 0, 
    "minutes": 0, 
    "seconds": 0
}

font = pygame.font.SysFont('Arial', 25)

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
    global time

    now = datetime.now()
    current_time_ms = now.timestamp() * 1000
    
    # Hores amb fracció de minuts (format 12 hores)
    time["hours"] = (current_time_ms / 3600000) % 12

    # Minuts amb fracció de segons    
    time["minutes"] = (current_time_ms / 60000) % 60

    # Segons amb fracció de mil·lisegons
    time["seconds"] = (current_time_ms / 1000) % 60

def app_draw():
    screen.fill(BLACK)
    utils.draw_grid(pygame, screen, 50)

    offset = -90
    center = {'x': 325, 'y': 250}
    center_tuple = tuple(center.values())
    radius = 200

    # Dibujamos horas
    degrees_per_hour = (360 / 12)
    hour_angle = (degrees_per_hour * time["hours"]) + offset
    hour = utils.point_on_circle(center, radius * 0.4, hour_angle)
    hour_tuple = (hour["x"], hour["y"])
    pygame.draw.line(screen, WHITE, center_tuple, hour_tuple, 10)

    # Dibujamos minutos
    degrees_per_hour = (360 / 60)
    minute_angle = (degrees_per_hour * time["minutes"]) + offset
    minute = utils.point_on_circle(center, radius * 0.7, minute_angle)
    minute_tuple = (minute["x"], minute["y"])
    pygame.draw.line(screen, BLUE, center_tuple, minute_tuple, 5)

    # Dibujamos segundos
    degrees_per_hour = (360 / 60)
    second_angle = (degrees_per_hour * time["seconds"]) + offset
    second = utils.point_on_circle(center, radius * 0.9, second_angle)
    second_tuple = (second["x"], second["y"])
    pygame.draw.line(screen, RED, center_tuple, second_tuple, 2)

    # Dibujamos números
    for n in range(1, 13):
        angle = (360 / 12) * n + offset
        pos_n = utils.point_on_circle(center, radius, angle)
        text = font.render(str(n), True, WHITE)
        screen.blit(text, tuple(pos_n.values()))

    pygame.display.update()

if __name__ == '__main__':
    main()