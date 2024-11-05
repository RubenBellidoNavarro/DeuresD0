#Arxiu exercici013.py
import pygame
import sys
import os
import utils

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 013')

path = os.path.join(os.path.dirname(__file__), './assets/exercici013/car.png')
img_car = pygame.image.load(path).convert_alpha()
img_car = utils.scale_image(pygame, img_car, target_width=15)

path = os.path.join(os.path.dirname(__file__), './assets/exercici013/circuit.png')
img_circuit = pygame.image.load(path).convert_alpha()
img_circuit = utils.scale_image(pygame, img_circuit, target_height=480)

car = {
    "x": 245,
    "y": 430,
    "angle": 270,
    "speed": 100,
    "img": img_car,
    "direction_x": "none",
    "direction_y": "none",
}

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car['direction_x'] = 'right'
            elif event.key == pygame.K_LEFT:
                car['direction_x'] = 'left'

            if event.key == pygame.K_UP:
                car['direction_y'] = 'up'
            elif event.key == pygame.K_DOWN:
                car['direction_y'] = 'down'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and car['direction_x'] == 'right':
                car['direction_x'] = 'none'
            elif event.key == pygame.K_LEFT and car['direction_x'] == 'left':
                car['direction_x'] = 'none'

            if event.key == pygame.K_UP and car['direction_y'] == 'up':
                car['direction_y'] = 'none'
            elif event.key == pygame.K_DOWN and car['direction_y'] == 'down':
                car['direction_y'] = 'none'
    return True

def app_run():
    delta_time = clock.get_time() / 1000
    displacement = car['speed'] * delta_time

    dx = car['direction_x']
    dy = car['direction_y']
    if dx == 'right':
        car['x'] += displacement
    elif dx == 'left':
        car['x'] -= displacement
    if dy == 'up':
        car['y'] -= displacement
    elif dy == 'down':
        car['y'] += displacement

    if dx == 'right' and dy == 'none':
        car['angle'] = 270
    elif dx == 'right' and dy == 'up':
        car['angle'] = 315
    elif dx == 'none' and dy == 'up':
        car['angle'] = 0
    elif dx == 'left' and dy == 'up':
        car['angle'] = 45
    elif dx == 'left' and dy == 'none':
        car['angle'] = 90
    elif dx == 'left' and dy == 'down':
        car['angle'] = 135
    elif dx == 'none' and dy == 'down':
        car['angle'] = 180
    elif dx == 'right' and dy == 'down':
        car['angle'] = 225

def app_draw():
    screen.blit(img_circuit, (0,0))
    
    rotated_img = pygame.transform.rotate(car["img"], car["angle"])
    rect = rotated_img.get_rect(center=(car["x"], car["y"]))
    screen.blit(rotated_img, rect)

    pygame.display.update()

if __name__ == '__main__':
    main()