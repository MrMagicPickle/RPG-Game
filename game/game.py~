import pygame
from pygame import *


WIDTH = 800
HEIGHT = 640
SCREEN_SIZE = pygame.Rect((0, 0, WIDTH, HEIGHT))
FPS = 60
TITLE = "HORROR_RPG"
TILE_SIZE = 32

PLAYER_SPEED = 4
PLAYER_RANGE = 8
INTERACTION_DELAY = 0.5


class Dialog():
    def __init__(self, pos):
        self.texts = []
        self.image = Surface((SCREEN_SIZE.width, SCREEN_SIZE.height))
        self.image.fill(Color("#800080"))
        self.rect = self.image.get_rect(topleft=pos)
        self.hasControl = False
        self.visible = False
        
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

    def show(self):
        self.hasControl = True
        self.visible = True

    def hide(self):
        self.hasControl = False
        self.visible = False

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
    
    def read(self, dialogFile):
        #read file and store in self.texts
        infile = open(dialogFile, 'r')
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

        

class Game():
    def __init__(self):
        self.dialog = Dialog((0, 442))
        

game = Game()

