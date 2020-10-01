import pygame
from pygame.locals import *

class Road:
    def __init__(self, gameDisplay, image, displayHeight):      
        self.speed = 0
        self.gameDisplay = gameDisplay
        self.image = image
        self.displayHeight = displayHeight

    def update(self, speed):
        self.speed += speed

    def spawn(self):
        self.newSpeed = self.speed % self.image.get_rect().height
        self.gameDisplay.blit(self.image, (0, self.newSpeed - self.image.get_rect().height))
        if self.newSpeed < self.displayHeight:
            self.gameDisplay.blit(self.image, (0, self.newSpeed))