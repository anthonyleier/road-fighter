import os
import sys
import pygame
from dotenv import load_dotenv
from objects.enemy import Enemy
from objects.player import Player


load_dotenv()
DISPLAY_WIDTH = int(os.environ.get('DISPLAY_WIDTH'))
DISPLAY_HEIGHT = int(os.environ.get('DISPLAY_HEIGHT'))


distance = 0
fuel = 100


def startEngine():
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Road Fighter')
    clock = pygame.time.Clock()
    return screen, clock


def startTexts():
    pygame.font.init()
    texts = pygame.font.Font('./sprites/font.ttf', 30)
    return texts


def loadPlayer(playerImage):
    player = Player(playerImage, 400, 600, 5)
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)
    return player, playerGroup


def loadEnemies(enemyImage):
    enemy1 = Enemy(enemyImage)
    enemy2 = Enemy(enemyImage)
    enemy3 = Enemy(enemyImage)
    enemy4 = Enemy(enemyImage)

    enemies = pygame.sprite.Group()
    enemies.add(enemy1)
    enemies.add(enemy2)
    enemies.add(enemy3)
    enemies.add(enemy4)

    return enemies


def catchEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def displayScreen(screen, screenStart):
    screen.blit(screenStart, (0, 0))


def catchControllerEvents(player, road, enemies):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        gameRunning = True
        return gameRunning

    if keys[pygame.K_LEFT]:
        player.update("left")

    if keys[pygame.K_RIGHT]:
        player.update("right")

    if keys[pygame.K_z]:
        road.update(20)
        # distance += 1
        enemies.update(4)

    else:
        enemies.update(-5)


def catchCollisions(player, enemies):
    collision = pygame.sprite.spritecollide(player, enemies, False)
    return collision


def drawHUD(screen, texts):
    title = texts.render('ROAD FIGTHER', False, (255, 255, 255))
    distanceText1 = texts.render('DISTANCE:', False, (255, 255, 255))
    distanceText2 = texts.render(str(distance), False, (255, 255, 255))
    fuelText1 = texts.render('FUEL:', False, (255, 255, 255))
    fuelText2 = texts.render(str(fuel), False, (255, 255, 255))

    margin = DISPLAY_WIDTH * 0.683
    screen.blit(title, (margin, 100))
    screen.blit(distanceText1, (margin, 300))
    screen.blit(distanceText2, (margin, 350))
    screen.blit(fuelText1, (margin, 500))
    screen.blit(fuelText2, (margin, 550))
