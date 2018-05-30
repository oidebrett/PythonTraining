from random import randint
import pygame

pygame.init()

#Initialise the screen
xmax = 600 #Width of screen in pixels
ymax = 600 #Height of screen in pixels
screen = pygame.display.set_mode((xmax, ymax), 0, 24) #New 24-bit screen
