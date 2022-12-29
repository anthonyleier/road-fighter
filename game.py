import pygame
from functions import catchEvents, catchControllerEvents, catchCollisions, drawHUD, displayScreen


def runGame(screen, clock, texts, player, playerGroup, enemies, road):
    gameRunning = False
    gameOver = False
    screenStart = pygame.image.load('./screens/start.png').convert()
    screenEnd = pygame.image.load('./screens/end.png').convert()

    while True:
        # Configure frame
        screen.fill((0, 0, 0))
        clock.tick(60)

        catchEvents()
        playPressed = catchControllerEvents(player, road, enemies)

        if playPressed and not gameRunning:
            gameRunning = True

        if not gameRunning:
            displayScreen(screen, screenStart)

        if gameOver:
            displayScreen(screen, screenEnd)

        if gameRunning and not gameOver:
            drawHUD(screen, texts)

            road.spawn()
            enemies.draw(screen)
            playerGroup.draw(screen)

            gameOver = catchCollisions(player, enemies)

        pygame.display.flip()
