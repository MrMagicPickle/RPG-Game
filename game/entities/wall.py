import pygame
from pygame import *
from entity import *

class Wall(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#FF0000"), pos, *groups)


