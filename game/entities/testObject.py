import pygame
from pygame import *
from interactable import *


class TestObject(Interactable):
    def __init__(self, name, color, pos, desc, *groups):
        super().__init__(color, desc, pos, *groups)
        self.name = name
        

