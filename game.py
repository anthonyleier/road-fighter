import pygame
from objects.road import Road
from objects.player import Player
from objects.enemy import Enemy
from pygame.locals import *

#Env Variables
play = True
displayWidth = 800
displayHeight = 800
displayDimensions = displayWidth, displayHeight

#Start Pygame Engine
pygame.init()
gameDisplay = pygame.display.set_mode(displayDimensions)
pygame.display.set_caption('Road Fighter')
fpsClock = pygame.time.Clock()
FPS = 120

#Loading Images
menu = "menu"
gameOver = "gameOver"

playerImage = pygame.image.load('./sprites/player.png')
enemyImage = pygame.image.load('./sprites/enemy.png')
roadImage = pygame.image.load('./sprites/road.png').convert()

#Define Objects
player1 = Player(gameDisplay, playerImage, displayDimensions)
road = Road(gameDisplay, roadImage, displayHeight)
enemy1 = Enemy(gameDisplay, enemyImage)
enemy2 = Enemy(gameDisplay, enemyImage)
enemy3 = Enemy(gameDisplay, enemyImage)
enemy4 = Enemy(gameDisplay, enemyImage)

#Start Time
last = pygame.time.get_ticks()

#Catch Events
def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

#Main Loop
while play:

    #Engine Configs
    now = pygame.time.get_ticks() 
    fpsClock.tick(FPS)
    events()

    #Keyboard Controller
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.left()
    if keys[pygame.K_RIGHT]:
        player1.right()
    if keys[pygame.K_z]:
        road.update(10)
        enemy1.slow()
        enemy2.slow()
        enemy3.slow()
        enemy4.slow()
    else:
        enemy1.fast()
        enemy2.fast()
        enemy3.fast()
        enemy4.fast()

    #Spawn Objects
    road.spawn()
    enemy1.spawn()
    enemy2.spawn()
    enemy3.spawn()
    enemy4.spawn()
    player1.spawn()

    #Update Display
    pygame.display.update()