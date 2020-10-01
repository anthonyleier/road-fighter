import pygame, random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.posX = random.randrange(220, 560)
        self.posY = random.randrange(0, 800) * -1
        self.rect.center = [self.posX, self.posY]

    def update(self, speed):
        if self.posY > 900:
            self.posX = random.randrange(220, 560)
            self.posY = -100
        self.speed = speed
        self.posY += speed
        self.rect.center = [self.posX, self.posY]
        