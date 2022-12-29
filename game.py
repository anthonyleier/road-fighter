import pygame
from functions import catchEvents, catchControllerEvents, catchCollisions, drawHUD, displayScreen, catchFuel


def runGame(screen, clock, texts, playerGroup, enemiesGroup, fuelsGroup, road):
    playerSprite = playerGroup.sprites()[0]

    gameRunning = False
    gameOver = False
    moreFuel = False
    distance = 0
    fuel = 100

    screenStart = pygame.image.load('screens/start.png').convert()
    screenEnd = pygame.image.load('screens/end.png').convert()

    while True:
        screen.fill((0, 0, 0))
        clock.tick(60)

        catchEvents()
        playPressed, accelerated = catchControllerEvents(road, playerSprite, enemiesGroup, fuelsGroup)

        if accelerated:
            distance += 1
            fuel -= 0.05

        if playPressed and not gameRunning:
            gameRunning = True

        if not gameRunning:
            displayScreen(screen, screenStart)

        if gameOver:
            displayScreen(screen, screenEnd)

        if gameRunning and not gameOver:
            drawHUD(screen, texts, distance, fuel)

            road.draw()
            fuelsGroup.draw(screen)
            enemiesGroup.draw(screen)
            playerGroup.draw(screen)

            gameOver = catchCollisions(playerSprite, enemiesGroup)
            moreFuel = catchFuel(playerSprite, fuelsGroup)

        if moreFuel:
            if fuel < 100:
                fuel += 10

            if fuel > 100:
                fuel = 100

        if fuel <= 0:
            gameOver = True

        pygame.display.flip()
