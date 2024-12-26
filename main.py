import pygame
import sys
from pygame.locals import *
import random
import time

# Define Constants
MOUSE_SIZE = (150, 150)
FPS = 60

score = 0
scoreIncrement = 1

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((626, 626), RESIZABLE)
pygame.display.set_caption("Shooter")
bgImg = pygame.image.load('assets/bg.png')

# Custom cursor settings
pygame.mouse.set_visible(False)
cursorImg = pygame.image.load('assets/rifle.png')
cursorImg = pygame.transform.scale(cursorImg, MOUSE_SIZE)

# Setting coordinates of fish
fishImg = pygame.image.load('assets/fish.png')
newSize = (50, 50)
fishImg = pygame.transform.scale(fishImg, newSize)
fishCoords = [(50, 50), (202, 50), (353, 50), (504, 50),
              (50, 202), (202, 202), (353, 202), (504, 202),
              (50, 353), (202, 353), (353, 353), (504, 353),
              (50, 504), (202, 504), (353, 504), (504, 504)]

# Game Variables
gameRunning = True
clock = pygame.time.Clock()
randomfishCoord = random.choice(fishCoords)
fishTimer = 0
fishMoveInterval = 1000

while gameRunning:
    screen.blit(bgImg, (0, 0))

    deltaTime = clock.tick(FPS)

    fishTimer += deltaTime
    if fishTimer >= fishMoveInterval:
        randomfishCoord = random.choice(fishCoords)
        fishTimer = 0

    screen.blit(fishImg, randomfishCoord)
    mousePos = pygame.mouse.get_pos()
    screen.blit(cursorImg, (mousePos[0] - MOUSE_SIZE[0] // 2, mousePos[1] - MOUSE_SIZE[1] // 2))

    for event in pygame.event.get():
        if event.type == QUIT:
            gameRunning = False
        if event.type == MOUSEBUTTONDOWN:
            if pygame.Rect(randomfishCoord, fishImg.get_size()).collidepoint(event.pos):
                score += scoreIncrement
                print(f"Score: {score}")
                randomfishCoord = random.choice(fishCoords)

    pygame.display.update()

sys.exit()
