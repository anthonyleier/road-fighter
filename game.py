import pygame
from functions import catchEvents, catchControllerEvents, catchCollisions, drawHUD, displayScreen


def runGame(screen, clock, texts, playerGroup, enemiesGroup, road):
    playerSprite = playerGroup.sprites()[0]

    gameRunning = False
    gameOver = False

    screenStart = pygame.image.load('./screens/start.png').convert()
    screenEnd = pygame.image.load('./screens/end.png').convert()

    while True:
        screen.fill((0, 0, 0))
        clock.tick(60)

        catchEvents()
        playPressed = catchControllerEvents(playerSprite, road, enemiesGroup)

        if playPressed and not gameRunning:
            gameRunning = True

        if not gameRunning:
            displayScreen(screen, screenStart)

        if gameOver:
            displayScreen(screen, screenEnd)

        if gameRunning and not gameOver:
            drawHUD(screen, texts)

            road.draw()
            enemiesGroup.draw(screen)
            playerGroup.draw(screen)

            gameOver = catchCollisions(playerSprite, enemiesGroup)

        pygame.display.flip()
