import pygame
from settings import *

class CameraLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, worldSize):
        super().__init__()
        self.target = target
        self.worldSize = worldSize

        #coordinates of our camera.
        self.cam = pygame.math.Vector2(0, 0)

        #add the target to our group.
        if self.target:
            self.add(target)



    def update(self, *args):

        super().update(*args)
        if self.target:
            l, t, _, _ = self.target.rect
            
            x = -l + SCREENSIZE.width/2
            y = -t + SCREENSIZE.height/2


            #edge limits.
            rightLimit = -(self.worldSize.width - SCREENSIZE.width)
            leftLimit = 0
            topLimit = 0
            bottomLimit = -(self.worldSize.height - SCREENSIZE.height)

            #prevent camera from crossing edges. 
            x = max(rightLimit, x)
            x = min(leftLimit, x)

            y = max(bottomLimit, y)
            y = min(topLimit, y)

            self.cam.x = x
            self.cam.y = y

    def draw(self, surface):
        spriteDict = self.spritedict
        for spr in self.sprites():
            rec = spriteDict[spr]
            newRect = surface.blit(spr.image, spr.rect.move(self.cam))
            
class Map:
    def __init__(self, filename):
        self.data = []
        file = open(filename, 'r')
        for line in file:
            self.data.append(line.strip())
        file.close()

        self.width = len(self.data[0]) * TILESIZE
        self.height = len(self.data) * TILESIZE
        
