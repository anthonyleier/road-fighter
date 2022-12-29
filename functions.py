import os
import sys
import pygame
from dotenv import load_dotenv
from classes.fuel import Fuel
from classes.enemy import Enemy
from classes.player import Player


load_dotenv()
DISPLAY_WIDTH = int(os.environ.get('DISPLAY_WIDTH'))
DISPLAY_HEIGHT = int(os.environ.get('DISPLAY_HEIGHT'))
QTY_ENEMIES = int(os.environ.get('QTY_ENEMIES'))
QTY_FUEL = int(os.environ.get('QTY_FUEL'))


def startEngine():
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Road Fighter')
    clock = pygame.time.Clock()
    return screen, clock


def startTexts():
    pygame.font.init()
    texts = pygame.font.Font('sprites/font.ttf', 30)
    return texts


def loadPlayerGroup():
    player = Player(400, 600, 5)
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)
    return playerGroup


def loadEnemiesGroup():
    enemiesGroup = pygame.sprite.Group()
    for _ in range(QTY_ENEMIES):
        enemiesGroup.add(Enemy())
    return enemiesGroup


def loadFuelsGroup():
    fuelsGroup = pygame.sprite.Group()
    for _ in range(QTY_FUEL):
        fuelsGroup.add(Fuel())
    return fuelsGroup


def catchEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def displayScreen(screen, image):
    screen.blit(image, (0, 0))


def catchControllerEvents(road, playerSprite, enemiesGroup, fuelsGroup):
    keys = pygame.key.get_pressed()
    playPressed = False
    accelerated = False

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    if keys[pygame.K_RETURN]:
        playPressed = True

    if keys[pygame.K_LEFT]:
        playerSprite.update("left")

    if keys[pygame.K_RIGHT]:
        playerSprite.update("right")

    if keys[pygame.K_z]:
        road.update(20)
        enemiesGroup.update(4)
        fuelsGroup.update(4)
        accelerated = True

    else:
        enemiesGroup.update(-5)
        fuelsGroup.update(-5)

    return playPressed, accelerated


def catchCollisions(playerSprite, enemiesGroup):
    collision = pygame.sprite.spritecollide(playerSprite, enemiesGroup, False)
    return collision


def catchFuel(playerSprite, fuelsGroup):
    moreFuel = pygame.sprite.spritecollide(playerSprite, fuelsGroup, False)
    if moreFuel:
        for fuel in fuelsGroup.sprites():
            fuel.posY = 5000
    return moreFuel


def drawHUD(screen, texts, distance, fuel):
    fuel = int(fuel)
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
