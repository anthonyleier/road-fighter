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

initialX = 400
initialY = 400

def setPlayerPosition(x, y):
    gameDisplay.blit(player, (x, y))

def controller(key):

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            controller(event.key)
    
    setPlayerPosition(currentX, currentY)
       
    pygame.display.update()
