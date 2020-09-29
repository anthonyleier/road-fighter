import pygame
from pygame.locals import *

displayWidth = 800
displayHeight = 800
displayDimensions = displayWidth, displayHeight

pygame.init()
gameDisplay = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption('Road Fighter')
fpsClock = pygame.time.Clock()

player = pygame.image.load('./sprites/player.png')
player = pygame.transform.scale(player, (int(displayWidth/20), int(displayHeight/20)))
mainRoad = pygame.image.load('./sprites/mainRoad.png')

FPS = 60
speed = 10
delay = 10
playerX = int(displayHeight / 2)
playerY = int(displayWidth * 3/4)

roadX = 100
roadY = int(displayWidth / 2)

def setPlayerPosition(x, y):
    gameDisplay.blit(player, (x, y))

def setRoadPosition(x, y):
    gameDisplay.blit(mainRoad, (x, y))
    
while True:
    fpsClock.tick(FPS)
    pygame.time.delay(delay)
    gameDisplay.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= speed
    if keys[pygame.K_RIGHT]:
        playerX += speed

    setRoadPosition(roadX, roadY)
    setPlayerPosition(playerX, playerY)
    
    myfont = pygame.font.SysFont("Arial", 30)
    label = myfont.render("Road Fighter", 1, (255,255,255))
    gameDisplay.blit(label, (325, 100))
    pygame.display.update()
