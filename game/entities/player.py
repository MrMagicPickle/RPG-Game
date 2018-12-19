import pygame
from entity import *
from pygame import *
from testObject import *



class Player(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#00FF00"), pos)
        self.vel = pygame.math.Vector2((0, 0))
        self.speed = PLAYER_SPEED
        self.range = PLAYER_RANGE
        self.facing = "down"
        self.interactionDelay = 0
        self.hasControl = True

    def hasCollided(self):
        # kind of hacky but it should work for now.
        entityGroup = self.groups()[0]
        for spr in (pygame.sprite.spritecollide(self, entityGroup, False)):
            if not isinstance(spr, Player):
                # collision happened.
                return True
        return False


    def getCollidedEntity(self):
        entityGroup = self.groups()[0]
        aObject = None
        shortestDistance = (TILE_SIZE // 2) + 1
        centerX = (self.rect.left + self.rect.right) // 2
        centerY = (self.rect.top + self.rect.bottom) // 2
        for spr in (pygame.sprite.spritecollide(self, entityGroup, False)):
            if isinstance(spr, TestObject):
                if self.facing == "up" or self.facing == "down":
                    objectCenterX = (spr.rect.left + spr.rect.right) // 2
                    distance = abs(objectCenterX - centerX)
                elif self. facing == "left" or self.facing == "right":
                    objectCenterY = (spr.rect.top + spr.rect.bottom) // 2
                    distance = abs(objectCenterY - centerY)
                if distance < shortestDistance:
                    aObject = spr
                    shortestDistance = distance
        return aObject


    def update(self):
        # get pressed key.
        pressed = pygame.key.get_pressed()


        # object interaction
        if self.interactionDelay > 0:
            self.interactionDelay += 1
        if self.interactionDelay >= FPS * INTERACTION_DELAY:
            self.interactionDelay = 0
        

        # movement
        self.vel.x = 0
        self.vel.y = 0

        if self.hasControl:
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
            if pressed[pygame.K_z] and self.interactionDelay == 0:
                #check whether the object is legit.
                self.tryInteract()
                
        #exit interact button.
        if pressed[pygame.K_x]:
            self.hasControl = True
            game.dialog.hide = True
            game.dialog.hasControl = False
            
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



    def tryInteract(self):
        targetEntity = self.getInteractEntity()
        
        if targetEntity is not None:
            #do something.
            self.interact(targetEntity)

    def getInteractEntity(self):
        prevX = self.rect.left
        prevY = self.rect.top
        if self.facing == "up":
            self.rect.top -= self.range
        elif self.facing == "down":
            self.rect.top += self.range
        elif self.facing == "left":
            self.rect.left -= self.range
        elif self.facing == "right":
            self.rect.left += self.range
            
        entity = self.getCollidedEntity()
        
        if entity is not None:
            self.interactionDelay += 1
            
        self.rect.left = prevX
        self.rect.top = prevY

        return entity

        
        

    def interact(self, target):
        #freeze player control.
        print("interacting with " + target.name)
        if self.hasControl:
            self.hasControl = False

            game.dialog.hide = False
            
