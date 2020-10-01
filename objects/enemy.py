import pygame, random
from pygame.locals import *

class Enemy:
    def __init__(self, gameDisplay, image):
        self.gameDisplay = gameDisplay
        self.image = image
        self.positionX = random.randrange(220, 560)
        self.positionY = random.randrange(0, 800) * -1

    def fast(self):
        self.positionY -= 5
    
    def slow(self):
        self.positionY += 4

    def spawn(self):
        self.gameDisplay.blit(self.image, (self.positionX, self.positionY))
        self.recalculate()
        
    def recalculate(self):
        if self.positionY > 800:
            self.positionX = random.randrange(220, 560)
            self.positionY = -100
