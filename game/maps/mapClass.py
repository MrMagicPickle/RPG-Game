import pygame
from pygame import *


import sys
import os
sys.path.append(os.path.abspath('..'))
from game import *


class Map:
    def __init__(self, filename):
        self.data = []
        file = open(filename, 'r')
        for line in file:
            self.data.append(line.strip())
        file.close()

        self.width = len(self.data[0]) * TILE_SIZE
        self.height = len(self.data) * TILE_SIZE
