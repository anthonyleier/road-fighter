import pygame
from functions import catchEvents, catchControllerEvents, catchCollisions, drawHUD


gameStart = True
gameOver = False
distance = 0
fuel = 100


def startGame(screen, clock, texts, player, enemies, road):
    while True:
        catchEvents()

        # Initial config
        screen.fill((0, 0, 0))
        clock.tick(60)

        # Controller
        catchControllerEvents(player, road, enemies)

        # Spawn
        road.spawn()
        enemies.draw(screen)
        player[0].draw(screen)

        # Colliders
        # gameOver = catchCollisions(player, enemies)

        # HUD
        drawHUD(screen, texts, distance, fuel)

        pygame.display.flip()
