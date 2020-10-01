import pygame
from pygame.locals import *

class Road:
    def __init__(self, image, display, displayHeight):      
        self.speed = 0
        self.display = display
        self.image = image
        self.displayHeight = displayHeight

    def update(self, speed):
        self.speed += speed

    def spawn(self):
        self.newSpeed = self.speed % self.image.get_rect().height
        self.display.blit(self.image, (0, self.newSpeed - self.image.get_rect().height))
        if self.newSpeed < self.displayHeight:
            self.display.blit(self.image, (0, self.newSpeed))