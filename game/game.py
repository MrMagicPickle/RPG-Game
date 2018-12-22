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

#init pygame font.
pygame.font.init()
class Dialog():
    def __init__(self, pos):
        self.dialogues = dict()
        self.image = Surface((SCREEN_SIZE.width, SCREEN_SIZE.height))
        self.image.fill(Color("#800080"))
        self.rect = self.image.get_rect(topleft=pos)
        self.hasControl = False
        self.textFont = pygame.font.SysFont("Comic Sans", 35)
        self.visible = False
        self.formattedTexts = None

        self.rowCharLimit = 65
        self.rowNum = 6
        
        self.interactionDelay = 0
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    #TODO: Global interactionDelay maybe?
    def update(self):
        # object interaction variables
        if self.interactionDelay > 0:
            self.interactionDelay += 1
        if self.interactionDelay >= FPS * INTERACTION_DELAY:
            self.interactionDelay = 0
        
        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        z = pressed[pygame.K_z]
        if self.hasControl:
            if up:
                print("Up key pressed on dialog")
            if down:
                print("Down key pressed on dialog")
            if z and self.interactionDelay == 0:
                self.nextPage()
            
                
        #update texts in the dialog here i guess?
        return

    def nextPage(self):
        print("next onegaishimasu")
        self.interactionDelay += 1
        if self.formattedTexts:
            #clear previous text.
            self.image.fill(Color("#800080"))            
            self.display()
        else:
            self.hide()
        
        
    def show(self):
        self.interactionDelay += 1  # stop multi-press on dialogue start
        self.hasControl = True
        self.visible = True

    def hide(self):
        self.hasControl = False
        self.visible = False
        #clear any text on the image.
        self.image.fill(Color("#800080"))
        self.interactionDelay = 0  # reset when close dialogue

        #give player control again.
        game.player.hasControl = True
        # feels abit hacky maybe we need a universal interaction delay for all non-movement key presses
        # not sure but feels like there could be potential bugs too
        game.player.interactionDelay = 1  # set player delay to cooldown

    def display(self):        
        rowHeight = 32
        for i in range (min(self.rowNum, len(self.formattedTexts))):
            currText = self.formattedTexts[i]
            textSurface = self.textFont.render(currText, True, (255,255,255))
            self.image.blit(textSurface, (0, i*rowHeight))


        #cut out whatever was displayed.
        if len(self.formattedTexts) > self.rowNum:
            self.formattedTexts = self.formattedTexts[i:]
        else:
            #edge case.            
            self.formattedTexts = None
            

    def formatText(self, text):
        n = len(text)
        start = 0
        end = 0

        formattedTexts = []
        
        while n > self.rowCharLimit:
            #find the last word of the text
            for k in range (self.rowCharLimit + start - 1, start, -1):
                if text[k] == " ":
                    end = k
                    break

            formattedTexts.append(text[start:end])

            #remaining text length
            truncatedTextLength = end - start + 1
            n -= truncatedTextLength

            #start pointer continues from cut off point.
            start = end + 1

        #add the remaining text.
        formattedTexts.append(text[start:len(text)])
        return formattedTexts
                

    def loadText(self, text):
        self.formattedTexts = self.formatText(text)

    def loadTextFromFile(self, key):
        text = self.dialogues[key]
        self.formattedTexts = self.formatText(text)
        
        
        
    '''
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
    '''
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
        self.player = None
        

game = Game()

