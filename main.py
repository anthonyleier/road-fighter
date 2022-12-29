from game import runGame
from classes.road import Road
from functions import startEngine, startTexts
from functions import loadPlayerGroup, loadEnemiesGroup, loadFuelsGroup


if __name__ == "__main__":
    screen, clock = startEngine()
    texts = startTexts()

    playerGroup = loadPlayerGroup()
    enemiesGroup = loadEnemiesGroup()
    fuelGroup = loadFuelsGroup()
    road = Road(screen)

    runGame(screen, clock, texts, playerGroup, enemiesGroup, fuelGroup, road)
