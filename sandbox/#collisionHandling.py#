'''
This is an extended version of cameraTest2.py file.

It builds upon the previous by adding collision handling behaviour.
'''

'''
This is an extension of the playerMovement.py file.

We're gonna build on top of it - with scrolling camera.
'''

import pygame
from pygame import *


#GLOBALS
SCREEN_SIZE = pygame.Rect((0, 0, 800, 640))
TILE_SIZE = 32 
        
        

    
    
#Extend this class when creating new entities.
class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        #sets the image to be a surface of a single tile.
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))

        self.image.fill(color)
        
        #the bounding box of the entity starting at top left position.
        self.rect = self.image.get_rect(topleft=pos)





#extends LayeredUpdates class but i have no idea why.. I might just follow suit.
#..cause i dont think its that important to understand this.
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
        spriteDict = self.spritedict
        for spr in self.sprites():
            rec = spriteDict[spr]
            newRect = surface.blit(spr.image, spr.rect.move(self.cam))
            
            

class Wall(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#FF0000"), pos, *groups)
        
        
    


class Player(Entity):
    def __init__(self, pos, *groups):
        super().__init__(pygame.Color("#00FF00"), pos)

        self.vel = pygame.math.Vector2((0, 0))
        self.speed = 8


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

    def hasCollided(self):        
        #kind of hacky but it should work for now.
        entityGroup = self.groups()[0]
        
        for spr in (pygame.sprite.spritecollide(self, entityGroup, False)):
            if not isinstance(spr, Player):
                #collision happened.
                return True
        return False
                

        
    

        
    


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()


    level = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "W                                          W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",]




    levelWidth = len(level[0]) * TILE_SIZE
    levelHeight = len(level) * TILE_SIZE

    player = Player((TILE_SIZE, levelHeight- 2*TILE_SIZE))    

    print("LEVEL height: " + str(levelHeight))
    print("Screen height: " + str(SCREEN_SIZE.height))
    entities = CameraLayeredUpdates(player, pygame.Rect(0, 0, levelWidth, levelHeight))

    #wall sprite group.
    walls = pygame.sprite.Group()

    #path sprite group.
    paths = pygame.sprite.Group()

    
    #build level.
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                #its in both walls sprite group and entities sprite group.
                Wall((x,y), walls, entities)

                
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        entities.update()
        
        screen.fill((0, 0, 0))
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)
    
    



if __name__ == "__main__":
    main()
