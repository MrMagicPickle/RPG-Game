import sys
import pygame
from pygame import *
from game import *

#-- Map.
sys.path.append("maps")
from mapClass import *


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

    level = Map("maps/empty.txt")

    #init our dialog.
    dialog = Dialog((0, 442))
    game.dialog = dialog
    
    #for now..
    game.dialog.read("../sandbox/dialog/dialogues.txt")
    
    levelWidth = level.width
    levelHeight = level.height

    player = Player((TILE_SIZE, levelHeight - 2 * TILE_SIZE))
    game.player = player
    print("LEVEL height: " + str(levelHeight))
    print("Screen height: " + str(SCREEN_SIZE.height))
    entities = CameraLayeredUpdates(player, pygame.Rect(0, 0, levelWidth, levelHeight))

    # wall sprite group.
    walls = pygame.sprite.Group()

    # path sprite group.
    paths = pygame.sprite.Group()

    # interactable sprite group.
    interactables = pygame.sprite.Group()

    # build level.
    x = y = 0
    for row in level.data:
        for col in row:
            if col == "W":
                # its in both walls sprite group and entities sprite group.
                Wall((x, y), walls, entities)

            x += TILE_SIZE
        y += TILE_SIZE
        x = 0

    desc = "dslfkjsdflk jslf jsadlf jasdklf jsdflk sadj flsadjf alsfdj salkjdf lkasjd flk kljhgjkdf gfjdk dfjkg dhfgjk dfgkj dfs hfgdk hsdfgjkfdsh kgjfdshg kdfsjgh dskjfgh sdkfgjh kdjsfhg sdkjfgh fdksjhg kdsjfgh dskjfgh kdsjhg kdfsjhg jkds hdskjg hdsgkjh dsfgkj dhsjk ghdsgk jfhds kjdfshg kdjsfgh dksfgh sdkjg hsdfkgj hdsjkfg hdfksjgh dfkjgh owrtw ktjnlwr tkjerwkly tnklyn ldgkhjf dlskgj ldsfgjrtgj eoirgj re gekrj tyerjk htykerj hyrekwjyh ekwyh eoryhj eorwiy hweoirhyiweoyr hnejkwh ewjrkh ywoqietjrewio hios hfoh woithiore hio heroigh erohi eroih eoihj eiorhjeroiytj oerij orei jewryh oiehrwy io"
    a = TestObject("a", pygame.Color("#0000FF"), (TILE_SIZE * 10, TILE_SIZE * 10),desc, interactables, entities)
    b = TestObject("b", pygame.Color("#00FFFF"), (TILE_SIZE * 11, TILE_SIZE * 10), "An untextured Box b", interactables, entities)

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
        for sprite in entities:
            entities.change_layer(sprite, sprite.rect.bottom)

        entities.update()
        game.dialog.update()
        screen.fill((0, 0, 0))
        entities.draw(screen)

        if game.dialog.visible:
            game.dialog.draw(screen)
            
        pygame.display.update()
        timer.tick(60)


if __name__ == "__main__":
    main()
