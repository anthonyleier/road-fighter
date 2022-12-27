import pygame
from functions import catchEvents, catchControllerEvents, catchCollisions, drawHUD


gameStart = True
gameOver = False


def startGame(screen, clock, texts, player, playerGroup, enemies, road):
    while True:
        catchEvents()

        # Initial config
        screen.fill((0, 0, 0))
        clock.tick(60)

        # HUD
        drawHUD(screen, texts)

        # Controller
        catchControllerEvents(player, road, enemies)

        # Spawn
        road.spawn()
        enemies.draw(screen)
        playerGroup.draw(screen)

        # Colliders
        collision = catchCollisions(player, enemies)

        if collision:
            return

        pygame.display.flip()
