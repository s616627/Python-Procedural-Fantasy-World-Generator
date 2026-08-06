import WorldGenerator
import displayFunctions

import pygame




play = False
rules = False

world = WorldGenerator.World(250,250)

world.printRegions()
pygame.init()
CLOCK = pygame.time.Clock()
running = True
displayFunctions.display_map(world)
pygame.quit()

