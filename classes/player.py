import os
import pygame
from dotenv import load_dotenv


load_dotenv()
GAME_BORDER_RIGHT = int(os.environ.get('GAME_BORDER_RIGHT'))
GAME_BORDER_LEFT = int(os.environ.get('GAME_BORDER_LEFT'))


class Player(pygame.sprite.Sprite):
    def __init__(self, posX, posY, speed):
        super().__init__()
        self.image = pygame.image.load('sprites/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.rect.center = [self.posX, self.posY]

    def update(self, direction):
        if direction == "right":
            if self.posX < GAME_BORDER_RIGHT:
                self.posX += self.speed

        if direction == 'left':
            if self.posX > GAME_BORDER_LEFT:
                self.posX -= self.speed

        self.rect.center = [self.posX, self.posY]
