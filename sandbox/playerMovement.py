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
        self.image = Surface((TILE_SIZE, TILE_SIZE))

        self.image.fill(color)
        
        #the bounding box of the entity starting at top left position.
        self.rect = self.image.get_rect(topleft=pos)


    


class Player(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#00FF00"), pos)

        self.vel = pygame.math.Vector2((0, 0))
        self.speed = 8


    def update(self):
        #get pressed key.
        pressed = pygame.key.get_pressed()

        up = pressed[K_UP]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]
        down = pressed[K_DOWN]


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


        #update our position.
        self.rect.left += self.vel.x
        self.rect.top += self.vel.y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        
    

        
    


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()


    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P    PPPPPPPP                              P",
        "P                                          P",
        "P                          PPPPPPP         P",
        "P                 PPPPPP                   P",
        "P                                          P",
        "P         PPPPPPP                          P",
        "P                                          P",
        "P                     PPPPPP               P",
        "P                                          P",
        "P   PPPPPPPPPPP                            P",
        "P                                          P",
        "P                 PPPPPPPPPPP              P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]


    player = Player((TILE_SIZE, SCREEN_SIZE.height-(2*TILE_SIZE)))


    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return
        player.update()
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.update()
        timer.tick(60)
    
    



if __name__ == "__main__":
    main()
