import pygame, sys
from objects.player import Player
from objects.road import Road
from objects.enemy import Enemy

#Env Variables
displayWidth = 800
displayHeight = 800

#Start Pygame Engine
pygame.init()
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Road Fighter')
clock = pygame.time.Clock()

#Loading Images
playerImage = pygame.image.load('./sprites/player.png').convert()
enemyImage = pygame.image.load('./sprites/enemy.png').convert()
roadImage = pygame.image.load('./sprites/road.png').convert()

#Define Objects
player1 = Player(playerImage, 400, 600, 5)
players = pygame.sprite.Group()
players.add(player1)

enemy1 = Enemy(enemyImage)
enemy2 = Enemy(enemyImage)
enemy3 = Enemy(enemyImage)
enemy4 = Enemy(enemyImage)
enemys = pygame.sprite.Group()
enemys.add(enemy1)
enemys.add(enemy2)
enemys.add(enemy3)
enemys.add(enemy4)

road = Road(roadImage, screen, displayHeight)

#Catch Events
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#Main Loop
while True:
    events()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        players.update("left")
    if keys[pygame.K_RIGHT]:
        players.update("right")
    if keys[pygame.K_z]:
        road.update(20)
        enemys.update(4)
    else:
        enemys.update(-5)

    road.spawn()
    enemys.draw(screen)
    players.draw(screen)
    if pygame.sprite.spritecollide(player1, enemys, False):
        print("Bateu")
    pygame.display.flip()