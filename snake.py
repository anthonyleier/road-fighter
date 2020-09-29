import pygame, random
from pygame.locals import *

def onGridRandom():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def outScreen(snakeHead):
    x, y = snakeHead

    if x < 0:
        x = 590
    if x > 590:
        x = 0
    if y < 0:
        y = 590
    if y > 590:
        y = 0
        
    return x, y

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 255, 0))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_pos = onGridRandom()

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
    
    if collision(snake[0], apple_pos):
        apple_pos = onGridRandom()
        snake.append((0,0))
  
    for i in range(len(snake)-1,0,-1):
        if collision(snake[0], snake[i]):
            pygame.quit()

    snake[0] = outScreen(snake[0])

    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
    
    pygame.display.update()
