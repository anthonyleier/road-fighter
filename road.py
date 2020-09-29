import pygame
from pygame.locals import *

displayWidth = 800
displayHeight = 800
displayDimensions = displayWidth, displayHeight

pygame.init()
gameDisplay = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption('Road Fighter')

player = pygame.image.load('./sprites/player.png')
player = pygame.transform.scale(player, (int(displayWidth/20), int(displayHeight/20)))

currentX = 400
currentY = 400
speed = 10

def setPlayerPosition(x, y):
    gameDisplay.blit(player, (x, y))
    
while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        currentY -= speed
    if keys[pygame.K_DOWN]:
        currentY += speed
    if keys[pygame.K_LEFT]:
        currentX -= speed
    if keys[pygame.K_RIGHT]:
        currentX += speed

    gameDisplay.fill((0,0,0))
    setPlayerPosition(currentX, currentY)
    pygame.display.update()
