import pygame
from pygame import *

SCREEN_SIZE = pygame.Rect((0, 0, 800, 640))

class Dialog():
    def __init__(self, pos):
        self.texts = []
        self.image = Surface((SCREEN_SIZE.width, SCREEN_SIZE.height))
        self.image.fill(Color("#800080"))
        self.rect = self.image.get_rect(topleft=pos)
        self.hasControl = False
        self.hide = True # change to self.visible

    #add hide() and show() functions.
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    timer = pygame.time.Clock()
    gameDialog = Dialog((0, 442))

    while True:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return

            if e.type == pygame.KEYDOWN and e.key == pygame.K_z:
                gameDialog.hide = False
                gameDialog.hasControl = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_x:
                gameDialog.hasControl = False
                gameDialog.hide = True

        screen.fill((0, 0, 0))                

        gameDialog.update()
        if not gameDialog.hide:
            gameDialog.draw(screen)
            

        pygame.display.update()
        timer.tick(60)
    


    
if __name__ == "__main__":
    main()
