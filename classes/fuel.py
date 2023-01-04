import os
import pygame
import random
from dotenv import load_dotenv


load_dotenv()
GAME_BORDER_LEFT = int(os.environ.get('GAME_BORDER_LEFT') or 240)
GAME_BORDER_RIGHT = int(os.environ.get('GAME_BORDER_RIGHT') or 580)


class Fuel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('sprites/fuel.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.posX = random.randint(GAME_BORDER_LEFT, GAME_BORDER_RIGHT)
        self.posY = random.randint(0, 800) * -1
        self.rect.center = [self.posX, self.posY]

    def update(self, speed):
        if self.posY > 900:
            self.posX = random.randint(GAME_BORDER_LEFT, GAME_BORDER_RIGHT)
            self.posY = random.randint(0, 100) * -1
        self.speed = speed
        self.posY += speed
        self.rect.center = [self.posX, self.posY]
