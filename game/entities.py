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
        self.speed = PLAYERSPEED
        self.range = PLAYERRANGE
        self.facing = "down"
        self.interaction_delay = 0


    def hasCollided(self):
        # kind of hacky but it should work for now.
        entityGroup = self.groups()[0]
        for spr in (pygame.sprite.spritecollide(self, entityGroup, False)):
            if not isinstance(spr, Player):
                # collision happened.
                return True
        return False


    def update(self):
        # get pressed key.
        pressed = pygame.key.get_pressed()



        # movement
        self.vel.x = 0
        self.vel.y = 0
        if pressed[pygame.K_UP]:
            self.facing = "up"
            self.vel.y = -self.speed
        if pressed[pygame.K_DOWN]:
            self.facing = "down"
            self.vel.y = self.speed
        if pressed[pygame.K_LEFT]:
            self.facing = "left"
            self.vel.x = -self.speed
        if pressed[pygame.K_RIGHT]:
            self.facing = "right"
            self.vel.x = self.speed

        # store our current positions in case of collision.
        prevX = self.rect.left
        prevY = self.rect.top

        # Update x position first.
        self.rect.left += self.vel.x

        # check for collisions.
        if self.hasCollided():
            self.rect.left = prevX

        # Update y position.
        self.rect.top += self.vel.y

        if self.hasCollided():
            self.rect.top = prevY



        # object interaction
        if self.interaction_delay > 0:
            self.interaction_delay += 1
        if self.interaction_delay >= FPS * INTERACTIONDELAY:
            self.interaction_delay = 0

        if pressed[pygame.K_z] and self.interaction_delay == 0:
            prevX = self.rect.left
            prevY = self.rect.top
            center_x = (self.rect.left + self.rect.right) // 2
            center_y = (self.rect.top + self.rect.bottom) // 2
            if self.facing == "up":
                self.rect.top -= self.range
            elif self.facing == "down":
                self.rect.top += self.range
            elif self.facing == "left":
                self.rect.left -= self.range
            elif self.facing == "right":
                self.rect.left += self.range
            if self.hasCollided():
                self.interaction_delay += 1
                print("Interact")
            self.rect.left = prevX
            self.rect.top = prevY


class Wall(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#FF0000"), pos, *groups)


class Object(Entity):
    def __init__(self, name, color, pos, *groups):
        super().__init__(color, pos, *groups)
        self.name = name