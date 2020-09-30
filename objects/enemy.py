import pygame
from pygame.locals import *

def enemyPrinter(gameDisplay, enemyImage, enemyX, enemyY):
    gameDisplay.blit(enemyImage, (enemyX, enemyY))