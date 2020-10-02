import pygame, sys
from objects.player import Player
from objects.road import Road
from objects.enemy import Enemy

#Env Variables
displayWidth = 1200
displayHeight = 800
gameIsStart = True
gameIsOver = False

#Start Pygame Engine
pygame.init()
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Road Fighter')
clock = pygame.time.Clock()

#Texts
pygame.font.init()
myfont = pygame.font.Font('./sprites/font.ttf', 30)
title = myfont.render('ROAD FIGTHER', False, (255, 255, 255))
distance = 0
fuel = 100

#Loading Images
playerImage = pygame.image.load('./sprites/player.png').convert_alpha()
enemyImage = pygame.image.load('./sprites/enemy.png').convert_alpha()
roadImage = pygame.image.load('./sprites/road.png').convert()
screenStart = pygame.image.load('./screens/start.png').convert()
screenEnd = pygame.image.load('./screens/end.png').convert()

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

def gameStart():
    screen.blit(screenStart, (0,0))

def gameOver():
    screen.blit(screenEnd, (0,0))

#Main Loop
while True:
    screen.fill((0,0,0))
    events()
    clock.tick(60)

    #Controller
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        gameIsStart = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        players.update("left")
    if keys[pygame.K_RIGHT]:
        players.update("right")
    if keys[pygame.K_z]:
        road.update(20)
        distance += 1
        enemys.update(4)
    else:
        enemys.update(-5)

    #Spawn
    road.spawn()
    enemys.draw(screen)
    players.draw(screen)

    #Colliders
    if pygame.sprite.spritecollide(player1, enemys, False):
        print("Bateu")
        gameIsOver = True

    #HUD
    distanceText1 = myfont.render('DISTANCE:', False, (255, 255, 255))
    distanceText2 = myfont.render(str(distance), False, (255, 255, 255))
    fuelText1 = myfont.render('FUEL:', False, (255, 255, 255))
    fuelText2 = myfont.render(str(fuel), False, (255, 255, 255))

    margin = 820
    screen.blit(title, (margin, 100))
    screen.blit(distanceText1, (margin, 300))
    screen.blit(distanceText2, (margin, 350))
    screen.blit(fuelText1, (margin, 500))
    screen.blit(fuelText2, (margin, 550))

    #StartScreen
    if gameIsStart:
        gameStart()

    #EndScreen
    if gameIsOver:
        gameOver()
        distance = 0
        fuel = 0

    pygame.display.flip()