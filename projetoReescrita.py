import pygame, sys

class Turtle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./sprites/player.png")
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

titi = Turtle()

turtles_group = pygame.sprite.Group()
turtles_group.add(titi)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    turtles_group.draw(screen)
    turtles_group.update()
    clock.tick(60)

    #https://www.youtube.com/watch?v=hDu8mcAlY4E