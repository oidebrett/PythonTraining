import pygame

#set up pygame
pygame.init()
window = pygame.display.set_mode((400,500))

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

pygame.draw.line(window, BLUE, (50,50),(250,50),4)
pygame.draw.line(window, GREEN, (100,250),(250,50),2)

pygame.display.update()
