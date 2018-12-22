import pygame
from pygame import *
from entity import *

class Wall(Entity):
    def __init__(self, pos, width, height, *groups):
        super().__init__(pygame.Color("#FF0000"), pos, *groups)
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft=pos)

