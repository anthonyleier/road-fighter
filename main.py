from game import runGame
from objects.road import Road
from functions import loadPlayerGroup, loadEnemiesGroup
from functions import startEngine, startTexts


if __name__ == "__main__":
    screen, clock = startEngine()
    texts = startTexts()

    playerGroup = loadPlayerGroup()
    enemiesGroup = loadEnemiesGroup()
    road = Road(screen)

    runGame(screen, clock, texts, playerGroup, enemiesGroup, road)
