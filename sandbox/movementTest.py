import pygame
import time


###################
#  G L O B A L S  #
###################

#tile size.
tileSize = 50

#display settings.
displayWidth = 1200
displayHeight = 800

#global window.
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("RPG v1.0")


class Camera():

    def __init__(self):
        self.pos = None

class Tile():
   
    def __init__(self, x, y, width=tileSize, height=tileSize):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        #the object that is placed on the tile
        self.owner = None

        self.draw()


    def draw(self):
        #call pygame.draw function here.
        #+1 to dimensions seem to make the lines thinner (like they are in the right position)
        #-- still tryna understand why that is the case though.
        #---UPDATE: oh, width of 50 means it ends at 49, since 0..49 == 50. +1 makes it end at
        #...the next square position.
        
        if self.owner is None:
            pygame.draw.rect(gameDisplay, (0, 0, 0), (self.x, self.y, self.width+1, self.height+1), 1)
        else:
            
        return None


    def blocked(self):
        if owner:
            return owner.blocked

        return False


    
pygame.init()

gameExit = False
#main loop ?
while True:

    for event in pygame.event.get():

        #to exit the app.
        if event.type == pygame.QUIT:
            pygame.quit()
            gameExit = True
            break
        
        #for now, we can exit the app using escape button.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                gameExit = True
                break



            
    #exit game.
    if gameExit:
        break


    
    
    #RENDER GRAPHICS.
    
    #color our surface.
    gameDisplay.fill((255, 255, 255))
    
    
    #--Generate Tiles.
    for x in range (0, 1200, tileSize):
        for y in range (0, 800, tileSize):
            aTile  = Tile(x, y, tileSize, tileSize)


    pygame.display.update()

