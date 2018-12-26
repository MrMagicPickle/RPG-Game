import pygame
from pygame import *

import sys
import os
sys.path.append(os.path.abspath('..'))
from game import *

sys.path.append("entities")
from player import *


class CameraLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, worldSize):
        super().__init__()
        #self.target = target
        self.worldSize = worldSize

        #coordinates of our camera.
        self.cam = pygame.math.Vector2(0, 0)

        #add the target to our group.
        #if self.target:
        #    self.add(target)

    def getTarget(self, target):
        self.target = target
        self.add(target)

    def update(self, *args):

        super().update(*args)
        if self.target:
            l, t, _, _ = self.target.rect
            
            x = -l + SCREEN_SIZE.width/2
            y = -t + SCREEN_SIZE.height/2


            #edge limits.
            rightLimit = -(self.worldSize.width - SCREEN_SIZE.width)
            leftLimit = 0
            topLimit = 0
            bottomLimit = -(self.worldSize.height - SCREEN_SIZE.height)

            #prevent camera from crossing edges. 
            x = max(rightLimit, x)
            x = min(leftLimit, x)

            y = max(bottomLimit, y)
            y = min(topLimit, y)

            self.cam.x = x
            self.cam.y = y

    def draw(self, surface):
        spriteDict = self.spritedict #unused
        for spr in self.sprites():
            rec = spriteDict[spr] #unused
            if isinstance(spr, Player):
                newRect = surface.blit(spr.image, spr.rect.move(self.cam.x, self.cam.y - 16))
            else:
                newRect = surface.blit(spr.image, spr.rect.move(self.cam))