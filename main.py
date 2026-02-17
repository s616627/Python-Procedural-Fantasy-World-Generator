import copy

import stringListFunctions
import nameFiles
import markovNameGenerator
from stringListFunctions import readFromFile
import Gods
import WorldGenerator
import displayFunctions

import random
import cardGame
import numpy
import pygame
import sys
import time



play = False
rules = False

world = WorldGenerator.World(250,250)

world.printRegions()
pygame.init()
CLOCK = pygame.time.Clock()
running = True
displayFunctions.display_map(world)
pygame.quit()

