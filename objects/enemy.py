import pygame
from pygame.locals import *

class Enemy:
    def __init__(self, gameDisplay, image, positionX, positionY):
        self.gameDisplay = gameDisplay
        self.image = image
        self.positionX = positionX
        self.positionY = positionY

    def fast(self):
        self.positionY -= 3
    
    def slow(self):
        self.positionY += 1

    def spawn(self):
        self.gameDisplay.blit(self.image, (self.positionX, self.positionY))
