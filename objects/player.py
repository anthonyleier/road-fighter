import pygame
from pygame.locals import *

class Player:
    positionX = 400
    positionY = 400
    speed = 10

    def __init__(self, gameDisplay, playerImage, displayDimensions):
        self.gameDisplay = gameDisplay
        self.image = playerImage
        self.displayWidth, self.displayHeight = displayDimensions
        self.positionX = int(self.displayHeight / 2)
        self.positionY = int(self.displayWidth * 3/4)

    def left(self):
        if self.positionX > 220:
            self.positionX -= self.speed

    def right(self):
        if self.positionX < 560:
            self.positionX += self.speed

    def spawn(self):
        self.gameDisplay.blit(self.image, (self.positionX, self.positionY))