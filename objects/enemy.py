import pygame, random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.posX = random.randrange(240, 580)
        self.posY = random.randrange(0, 800) * -1
        self.rect.center = [self.posX, self.posY]

    def update(self, speed):
        if self.posY > 900:
            self.posX = random.randrange(240, 580)
            self.posY = random.randrange(0, 100) * -1
        self.speed = speed
        self.posY += speed
        self.rect.center = [self.posX, self.posY]
        