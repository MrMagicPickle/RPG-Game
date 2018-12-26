import sys
import pygame
from pygame import *
from game import *

#-- Map.
sys.path.append("maps")
from mapClass import *
from level import *
#-- Camera.
sys.path.append("camera")
from scrollingCamera import *

#-- Entities.
sys.path.append("entities")
from player import *
from wall import *
from testObject import *

#-- Dialog.
from dialog import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()

    #init our dialog.
    dialog = Dialog((0, 442))
    game.dialog = dialog
    
    #for now..
    game.dialog.read("../sandbox/dialog/dialogues.txt")

    player = Player((0, 0))
    game.player = player

    # make level
    level = Level("maps/tempmap")
    level.buildLevel()
    level.playerStartPoint(player)
    level.entities.getTarget(player)


    print("LEVEL height: " + str(level.height))
    print("Screen height: " + str(SCREEN_SIZE.height))

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:                
                    return

                #Hmm... Sketchy code.
                if e.key == pygame.K_z:
                    if player.hasControl:
                        player.tryInteract()
                    elif game.dialog.hasControl:
                        game.dialog.nextPage()
                        


        # sprites closer to bottom are drawn above sprites closer to top
        for sprite in level.entities:
            level.entities.change_layer(sprite, sprite.rect.bottom)

        level.entities.update()
        game.dialog.update()
        screen.fill((0, 0, 0))
        screen.blit(level.background, level.background.get_rect().move(level.entities.cam))
        level.entities.draw(screen)

        if game.dialog.visible:
            game.dialog.draw(screen)
            
        pygame.display.update()
        timer.tick(60)


if __name__ == "__main__":
    main()
