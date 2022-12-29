import os
import pygame
from game import runGame
from objects.road import Road
from dotenv import load_dotenv
from functions import displayScreen
from functions import loadPlayer, loadEnemies
from functions import startEngine, startTexts


load_dotenv()
DISPLAY_WIDTH = int(os.environ.get('DISPLAY_WIDTH'))
DISPLAY_HEIGHT = int(os.environ.get('DISPLAY_HEIGHT'))


if __name__ == "__main__":
    screen, clock = startEngine()
    texts = startTexts()

    playerImage = pygame.image.load('./sprites/player.png').convert_alpha()
    enemyImage = pygame.image.load('./sprites/enemy.png').convert_alpha()
    roadImage = pygame.image.load('./sprites/road.png').convert()

    player, playerGroup = loadPlayer(playerImage)
    enemies = loadEnemies(enemyImage)
    road = Road(roadImage, screen, DISPLAY_HEIGHT)

    runGame(screen, clock, texts, player, playerGroup, enemies, road)
