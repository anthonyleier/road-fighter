import pygame
from time import sleep
from functions import drawHUD, displayScreen, addFuel
from functions import catchEvents, catchControllerEvents, catchCollisions, catchFuel
from sounds import startingMusic, endingMusic, emptyFuelSound, motorIdle, motorAccelerated, stopAllSounds


def runGame(screen, clock, texts, playerGroup, enemiesGroup, fuelsGroup, road):
    # Player sprite is the only sprite from playerGroup
    playerSprite = playerGroup.sprites()[0]

    # Incialize variables
    gameRunning = False
    gameOver = False
    moreFuel = False
    distance = 0
    fuel = 100

    # Screens
    screenStart = pygame.image.load('screens/start.png').convert()
    screenEnd = pygame.image.load('screens/end.png').convert()

    # Playing sounds control
    playingFuelSound = False
    playingMotorIdleSound = False
    playingMotorAcceleratedSound = False
    playingEndingSound = False
    startingMusic.play()

    while True:
        # Frame inicialization
        screen.fill((0, 0, 0))
        clock.tick(60)

        # Events and controller
        catchEvents()
        playPressed, accelerated = catchControllerEvents(road, playerSprite, enemiesGroup, fuelsGroup)

        # Start
        if playPressed and not gameRunning:
            gameRunning = True

        # Main menu
        if not gameRunning:
            displayScreen(screen, screenStart)

        # Game over
        if gameOver:
            sleep(0.3)
            displayScreen(screen, screenEnd)
            if not playingEndingSound:
                stopAllSounds()
                endingMusic.play()
                playingEndingSound = True

        # Gameplay
        if gameRunning and not gameOver:
            drawHUD(screen, texts, distance, fuel)

            # In Acceleration
            if accelerated:
                distance += 1
                fuel -= 0.05

                # Motor sound accelerated
                if not playingMotorAcceleratedSound:
                    motorIdle.stop()
                    playingMotorIdleSound = False
                    motorAccelerated.play()
                    playingMotorAcceleratedSound = True

            # Motor sound idle
            if not playingMotorIdleSound and not accelerated:
                motorAccelerated.stop()
                playingMotorAcceleratedSound = False
                motorIdle.play()
                playingMotorIdleSound = True

            # Draw objects
            road.draw()
            fuelsGroup.draw(screen)
            enemiesGroup.draw(screen)
            playerGroup.draw(screen)

            # Game collisions
            gameOver = catchCollisions(playerSprite, enemiesGroup)
            moreFuel = catchFuel(playerSprite, fuelsGroup)

            # Add fuel logic
            fuel = addFuel(fuel, moreFuel)

            # Endgame if fuel is empty
            if fuel <= 0:
                gameOver = True

            # Fuel sound warning
            if fuel <= 20 and not playingFuelSound:
                emptyFuelSound.play()
                playingFuelSound = True

            # Stop fuel sound warning
            if fuel > 20:
                emptyFuelSound.stop()
                playingFuelSound = False

        pygame.display.flip()
