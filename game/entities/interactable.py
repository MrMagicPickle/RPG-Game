import pygame
import os
import sys
sys.path.append(os.path.abspath('..'))
from game import *
from entity import *

class Interactable(Entity):
    def __init__(self, color, desc, pos, *groups):
        super().__init__(color, pos, *groups)        
        self.desc = desc

    def interact(self, target):
        game.dialog.show()
        game.dialog.loadText(self.desc)
        game.dialog.display()
        
