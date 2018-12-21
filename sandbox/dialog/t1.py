import pygame
from pygame import *

SCREEN_SIZE = pygame.Rect((0, 0, 800, 640))

class Dialog():
    def __init__(self, pos, surface):
        self.dialogues = dict()
        self.image = Surface((SCREEN_SIZE.width, SCREEN_SIZE.height))
        self.image.fill(Color("#800080"))
        self.rect = self.image.get_rect(topleft=pos)
        self.hasControl = False
        self.hide = True # change to self.visible
        self.textFont = pygame.font.SysFont("Comic Sans", 35)
        self.screen = surface

    #add hide() and show() functions.
    def draw(self):
        self.screen.blit(self.image, self.rect)

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

    def loadText(self, key):
        

        rowLength = 75
        text = self.dialogues[key]
        print(len(text))
        
        n = len(text)
        start = 0
        end = 0
        rowCounter = 0
        while n > rowLength:
            #find the end.
            for k in range (rowLength+start-1, start, -1):
                if text[k] == " ":
                    end = k
                    break
            print(len(text[start:end]))
            textSurface = self.textFont.render(text[start:end], True, (255,255,255))
            self.image.blit(textSurface, (0,rowCounter))

            rowCounter += 32

            truncatedTextLength = end - start + 1
            n -= truncatedTextLength
            
            start = end + 1
        #add remainder to next row.
        textSurface = self.textFont.render(text[start:len(text)], True, (255,255,255))
        self.image.blit(textSurface, (0, rowCounter))
            

            
        
        
        
        print(text)

        
        

    def read(self, file):
        #read file and store in self.texts
        infile = open(file, 'r')
        keys = []
        texts = []
        currText = ""
        startStoring = False
        for line in infile:
            line = line.strip('\n')
            line = line.split()
            
            if len(line) > 0:
                if line[0] == "-":
                    keys.append(line[1])
                    startStoring = True
                
                elif line[0] == "*":
                    texts.append(currText)
                    currText = ""
                    startStoring = False
                else:
                    if startStoring:
                        for k in range (len(line)):
                            currText += line[k]

                            if k != len(line)-1:
                                currText += " "

        for i in range (len(keys)):
            self.dialogues[keys[i]] = texts[i]

        
                
                


def main():

    pygame.init()
    #init font
    pygame.font.init()            
    screen = pygame.display.set_mode((800, 640))
    timer = pygame.time.Clock()
    gameDialog = Dialog((0, 442), screen)
    gameDialog.read("dialogues.txt")
    for key, val in gameDialog.dialogues.items():
        print("----")
        print("KEY: " + str(key))
        print("Value: ")
        print(val)
        
    print("Text of plant 1.0: " )
    #gameDialog.displayDialogue("-plant1.0-")

    print(" " )

    print("text of -intro1.1-")
    gameDialog.loadText("-intro1.1-")
    
        
        
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
            gameDialog.draw()
            

        pygame.display.update()
        timer.tick(60)
    


    
if __name__ == "__main__":
    main()
