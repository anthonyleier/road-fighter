import os
import pygame
from dotenv import load_dotenv


load_dotenv()
DISPLAY_HEIGHT = int(os.environ.get('DISPLAY_HEIGHT', 800))


class Road:
    def __init__(self, display):
        self.speed = 0
        self.display = display
        self.image = pygame.image.load('sprites/road.png').convert()

    def update(self, speed):
        self.speed += speed

    def draw(self):
        self.newSpeed = self.speed % self.image.get_rect().height
        self.display.blit(self.image, (0, self.newSpeed - self.image.get_rect().height))
        if self.newSpeed < DISPLAY_HEIGHT:
            self.display.blit(self.image, (0, self.newSpeed))
