import pygame
import objects.road as road
import objects.player as player
import objects.enemy as enemy
from pygame.locals import *

play = True
displayWidth = 800
displayHeight = 800
displayDimensions = displayWidth, displayHeight

pygame.init()
gameDisplay = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption('Road Fighter')
fpsClock = pygame.time.Clock()
FPS = 120

playerImage = pygame.image.load('./sprites/player.png')
enemyImage = pygame.image.load('./sprites/enemy.png')
roadImage = pygame.image.load('./sprites/road.png').convert()

playerX = int(displayHeight / 2)
playerY = int(displayWidth * 3/4)
enemyX = 400
enemyY = 400
playerSpeed = 10
roadSpeed = 0

def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

while play:
    fpsClock.tick(FPS)
    events()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > 220:
        playerX -= playerSpeed
    if keys[pygame.K_RIGHT] and playerX < 560:
        playerX += playerSpeed
    if keys[pygame.K_z]:
        roadSpeed += 10

    road.roadPrinter(gameDisplay, displayHeight, roadImage, roadSpeed)
    player.playerPrinter(gameDisplay, playerImage, playerX, playerY)
    enemy.enemyPrinter(gameDisplay, enemyImage, enemyX, enemyY)
    pygame.display.update()