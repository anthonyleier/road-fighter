import pygame
from functions import catchEvents, catchControllerEvents, catchCollisions, drawHUD, displayScreen


def startGame(screen, clock, texts, player, playerGroup, enemies, road):
    gameStart = False
    gameOver = False
    screenStart = pygame.image.load('./screens/start.png').convert()
    screenEnd = pygame.image.load('./screens/end.png').convert()

    while True:
        # Initial config
        screen.fill((0, 0, 0))
        clock.tick(60)

        if not gameStart:
            displayScreen(screen, screenStart)

        elif gameOver:
            displayScreen(screen, screenEnd)

        else:
            # Catch Events
            catchEvents()

            # HUD
            drawHUD(screen, texts)

            # Controller
            gameStart = catchControllerEvents(player, road, enemies)

            # Spawn
            road.spawn()
            enemies.draw(screen)
            playerGroup.draw(screen)

            # Colliders
            gameOver = catchCollisions(player, enemies)

        pygame.display.flip()
