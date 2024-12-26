import pygame
import sys
from pygame.locals import *
import random

# Define Constants
MOUSE_SIZE = (150, 150)
FPS = 60

score = 0
scoreIncrement = 1

# Initialize pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((626, 626), RESIZABLE)
pygame.display.set_caption("Shooter")
bgImg = pygame.image.load('assets/bg.png')

# Custom cursor settings
pygame.mouse.set_visible(False)
cursorImg = pygame.image.load('assets/rifle.png')
cursorImg = pygame.transform.scale(cursorImg, MOUSE_SIZE)

# Setting coordinates of fish
fishImg = pygame.image.load('assets/fish.png')
newSize = (100, 100)
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

#Setting up font
font = pygame.font.Font(None, 36)

#Load audio
gunshotHit = pygame.mixer.Sound('assets/audio/gunshotHit.mp3')
gunshotMiss = pygame.mixer.Sound('assets/audio/gunshotMiss.mp3')

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
                randomfishCoord = random.choice(fishCoords)
                gunshotHit.play()
            else:
                gunshotMiss.play()
    
    scoreText = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(scoreText, (10, 10))

    pygame.display.update()

sys.exit()