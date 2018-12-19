import pygame
from pygame import *


WIDTH = 800
HEIGHT = 640
SCREEN_SIZE = pygame.Rect((0, 0, WIDTH, HEIGHT))
FPS = 60
TITLE = "HORROR_RPG"
TILE_SIZE = 32

PLAYER_SPEED = 4
PLAYER_RANGE = 8
INTERACTION_DELAY = 0.5


class Dialog():
    def __init__(self, pos):
        self.texts = []
        self.image = Surface((SCREEN_SIZE.width, SCREEN_SIZE.height))
        self.image.fill(Color("#800080"))
        self.rect = self.image.get_rect(topleft=pos)
        self.hasControl = False
        self.hide = True
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        
        if self.hasControl:
            if up:
                print("Up key pressed on dialog")
            if down:
                print("Down key pressed on dialog")
            
        #update texts in the dialog here i guess?
        return

class Game():
    def __init__(self):
        self.dialog = Dialog((0, 442))
        

game = Game()

