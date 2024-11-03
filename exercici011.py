#Arxiu exercici011.py
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 011')

def main():
    is_looping = True

    global dir_x, pos_x, radi
    dir_x = 'none'
    pos_x = 100
    radi = 10 + (pos_x / 8)

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global dir_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dir_x = 'right'
            elif event.key == pygame.K_LEFT:
                dir_x = 'left'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if dir_x == 'right':
                    dir_x = 'none'
            elif event.key == pygame.K_LEFT:
                if dir_x == 'left':
                    dir_x = 'none'
    return True

def app_run():
    global pos_x, radi
    delta_time = clock.get_time() / 1000 # Convertir a segons

    speed = 100
    displacement = speed * delta_time

    if (dir_x == 'right'):
        pos_x += displacement
        radi = 10 + (pos_x / 8)
        limit_right = (pos_x + radi >= 640)
        if (limit_right):
            pos_x = 640 - radi
    elif (dir_x == 'left'):
        pos_x -= displacement
        radi = 10 + (pos_x / 8)
        limit_left = (pos_x - radi <= 0)
        if (limit_left):
            pos_x = radi

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Apreta les tecles (left/right)', True, BLACK)
    screen.blit(text, (50,50))

    pygame.draw.circle(screen, BLACK, (pos_x, 250), radi)

    pygame.display.update()

if __name__ == '__main__':
    main()