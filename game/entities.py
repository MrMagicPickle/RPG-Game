import pygame
from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        
        # sets the image to be a surface of a single tile.
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        
        # the bounding box of the entity starting at top left position.
        self.rect = self.image.get_rect(topleft=pos)
        
        
class Player(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#00FF00"), pos)

        self.vel = pygame.math.Vector2((0, 0))
        self.speed = 8

    def hasCollided(self):        
        #kind of hacky but it should work for now.
        entityGroup = self.groups()[0]
        
        for spr in (pygame.sprite.spritecollide(self, entityGroup, False)):
            if not isinstance(spr, Player):
                #collision happened.
                return True
        return False
        
    def update(self):
        #get pressed key.
        pressed = pygame.key.get_pressed()
 
        up = pressed[pygame.K_UP]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        down = pressed[pygame.K_DOWN]


        if up:
            self.vel.y = -self.speed
        if down:
            self.vel.y = self.speed
        if left:
            self.vel.x = -self.speed
        if right:
            self.vel.x = self.speed

        #if we're not moving...
        if not (left or right):
            self.vel.x = 0
        if not (up or down):
            self.vel.y = 0

        #store our current positions in case of collision.
        prevX = self.rect.left
        prevY = self.rect.top

        #Update x position first.
        self.rect.left += self.vel.x
        
        #check for collisions.
        if self.hasCollided():
            self.rect.left = prevX

        #Update y position.
        self.rect.top += self.vel.y

        if self.hasCollided():
            self.rect.top = prevY       


class Wall(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#FF0000"), pos, *groups)         

    
