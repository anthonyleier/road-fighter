import pygame
from pygame.locals import *

def playerPrinter(gameDisplay, playerImage, playerX, playerY):
    gameDisplay.blit(playerImage, (playerX, playerY))