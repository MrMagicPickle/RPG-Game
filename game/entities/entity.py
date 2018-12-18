import pygame
import os
import sys
sys.path.append(os.path.abspath('..'))
from game import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        
        # sets the image to be a surface of a single tile.
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        
        # the bounding box of the entity starting at top left position.
        self.rect = self.image.get_rect(topleft=pos)


    
        
