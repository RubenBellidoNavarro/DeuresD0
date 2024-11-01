#Arxiu exercici001.py
import pygame
import utils
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

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Exercici 002')

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
    
    #'HEADLINE NEWS'
    pygame.draw.rect(screen, RED, (50, 50, 550, 100))
    ARIAL_60 = pygame.font.SysFont('Arial', 60)
    headline_news = ARIAL_60.render('HEADLINE NEWS', True, WHITE)
    screen.blit(headline_news, (75, 75))
    
    #'World goes Wrong!'
    COURIER_NEW_40_bold = pygame.font.SysFont('Courier New', 40, True)
    world_goes_wrong = COURIER_NEW_40_bold.render('World goes Wrong!', True, BLACK)
    screen.blit(world_goes_wrong, (50,160))

    #'YEP#'
    yep = COURIER_NEW_40_bold.render('YEP#', True, GREEN)
    screen.blit(yep, (510,160))

    #'Lore ipsum...'
    ARIAL_28 = pygame.font.SysFont('Arial', 28)
    text1 = ARIAL_28.render("Lorem ipsum dolor sit amet, consectetur", True, BLACK)
    screen.blit(text1, (50, 250))
    text2 = ARIAL_28.render("adipiscing elit, sed do eiusmod tempor", True, BLACK)
    screen.blit(text2, (50, 285))
    text3 = ARIAL_28.render("incididunt ut labore et dolore magna aliqua.", True, BLACK)
    screen.blit(text3, (50, 320))

    pygame.display.update()

if __name__ == '__main__':
    main()