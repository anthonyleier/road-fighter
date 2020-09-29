import pygame
from pygame.locals import *

displayWidth = 800
displayHeight = 800
displayDimensions = displayWidth, displayHeight

pygame.init()
gameDisplay = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption('Road Fighter')
fpsClock = pygame.time.Clock()
FPS = 120

player = pygame.image.load('./sprites/player.png')
player = pygame.transform.scale(player, (int(displayWidth/20), int(displayHeight/20)))
playerSpeed = 10
playerX = int(displayHeight / 2)
playerY = int(displayWidth * 3/4)

road = pygame.image.load('./sprites/road.png').convert()
y = 0
def setPlayerPosition(x, y):
    gameDisplay.blit(player, (x, y))

def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

while True:
    fpsClock.tick(FPS)
    events()

    rel_y = y % road.get_rect().height
    gameDisplay.blit(road, (0, rel_y - road.get_rect().height))
    if rel_y < displayHeight:
        gameDisplay.blit(road, (0, rel_y))
    y += 1    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX -= playerSpeed
    if keys[pygame.K_RIGHT]:
        playerX += playerSpeed

    setPlayerPosition(playerX, playerY)
    pygame.display.update()