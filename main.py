import pygame
import sys
from pygame.locals import *

#Define Constatnts
MOUSE_SIZE = (150, 150)

pygame.init()
screen = pygame.display.set_mode((626, 626), RESIZABLE)
pygame.display.set_caption("Shooter")
bgImg = pygame.image.load('assets/bg.png')

#Custom cursor settings
pygame.mouse.set_visible(False)
cursorImg = pygame.image.load('assets/rifle.png')
cursorImg = pygame.transform.scale(cursorImg, MOUSE_SIZE)

gameRunning = True
while gameRunning:
    screen.blit(bgImg, (0, 0))
    
    mousePos = pygame.mouse.get_pos()
    screen.blit(cursorImg, mousePos)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            gameRunning = False
    
    pygame.display.update()
    
    
sys.exit()