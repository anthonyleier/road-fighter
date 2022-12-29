import pygame


pygame.init()
explosionSound = pygame.mixer.Sound('sounds/explosion.wav')
collectFuelSound = pygame.mixer.Sound('sounds/fuel.wav')
endingMusic = pygame.mixer.Sound('sounds/game_over.wav')
emptyFuelSound = pygame.mixer.Sound('sounds/empty_gas.wav')
startingMusic = pygame.mixer.Sound('sounds/game_start.wav')
motorIdle = pygame.mixer.Sound('sounds/motor_player.wav')
motorAccelerated = pygame.mixer.Sound('sounds/motor_player_accelerated.wav')


def stopAllSounds():
    explosionSound.stop()
    collectFuelSound.stop()
    endingMusic.stop()
    emptyFuelSound.stop()
    startingMusic.stop()
    motorIdle.stop()
    motorAccelerated.stop()
