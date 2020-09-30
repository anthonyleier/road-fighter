import pygame
from pygame.locals import *

def roadPrinter(gameDisplay, displayHeight, roadImage, roadSpeed):
    newRoadSpeed = roadSpeed % roadImage.get_rect().height
    gameDisplay.blit(roadImage, (0, newRoadSpeed - roadImage.get_rect().height))
    if newRoadSpeed < displayHeight:
        gameDisplay.blit(roadImage, (0, newRoadSpeed))