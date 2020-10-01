import pygame
from pygame.locals import *

class Player:
    def __init__(self, gameDisplay, playerImage, displayDimensions):
        self.gameDisplay = gameDisplay
        self.image = playerImage
        self.displayWidth, self.displayHeight = displayDimensions
        self.positionX = int(self.displayHeight / 2)
        self.positionY = int(self.displayWidth * 3/4)
        self.rect = self.image.get_rect(topleft = (self.positionX, self.positionY))
        self.speed = 3

    def left(self):
        self.newX = self.positionX - self.speed
        self.rect.move_ip(self.newX, self.positionY)

    def right(self):
        if self.positionX < 560:
            self.positionX += self.speed

    def spawn(self):
        self.gameDisplay.blit(self.image, self.rect)

    def detectCollision(self, entity):
        print("Eu:", self.positionX, self.positionY)
        print("Inimigo:", entity.positionX, entity.positionY)
        if self.positionX == entity.positionX:
            if self.positionY == entity.positionY:
                print("Bateu")