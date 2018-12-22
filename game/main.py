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

import pytmx


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()

    level = TiledMap("maps/tempmap")
    
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

    objectList = ["a", "b", "c"]
    objectDesc = [
        "Page 1 dslfkjsdflk jslf jsadlf jasdklf jsdflk sadj flsadjf alsfdj salkjdf lkasjd flk kljhgjkdf gfjdk dfjkg"
        " dhfgjk dfgkj dfs hfgdk hsdfgjkfdsh kgjfdshg kdfsjgh dskjfgh sdkfgjh kdjsfhg sdkjfgh fdksjhg kdsjfgh dskjfgh"
        " kdsjhg kdfsjhg jkds hdskjg hdsgkjh dsfgkj dhsjk ghdsgk jfhds kjdfshg kdjsfgh dksfgh sdkjg Page 2 hsdfkgj"
        " hdsjkfg hdfksjgh dfkjgh owrtw ktjnlwr tkjerwkly tnklyn ldgkhjf dlskgj ldsfgjrtgj eoirgj re gekrj tyerjk "
        "htykerj hyrekwjyh ekwyh eoryhj eorwiy hweoirhyiweoyr hnejkwh ewjrkh ywoqietjrewio hios hfoh woithiore hio"
        " heroigh erohi eroih eoihj eiorhjeroiytj oerij orei jewryh oiehrwy io",
        "An untextured Box b", "Far Away Box"]
    objectColors = ["#0000FF", "#FF00FF", "#00FFFF"]
    objectCount = 0
    # build level.
    background = level.bg
    mapObjects = level.data.objects
    # probably should make a class for building levels or some shit
    for ob in mapObjects:
        if ob.type == "Player":
            player.rect.left = ob.x
            player.rect.top = ob.y
        if ob.type == "Wall":
            Wall((ob.x, ob.y), ob.width, ob.height,  walls, entities)
        if ob.type == "Object":
            # maybe building objects can be split also idk
            print(objectCount)
            TestObject(objectList[objectCount], pygame.Color(objectColors[objectCount]), (ob.x, ob.y),
                       objectDesc[objectCount], interactables, entities)
            objectCount += 1

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        # sprites closer to bottom are drawn above sprites closer to top
        for sprite in entities:
            entities.change_layer(sprite, sprite.rect.bottom)

        entities.update()
        game.dialog.update()
        screen.fill((0, 0, 0))
        screen.blit(background, background.get_rect().move(entities.cam))
        entities.draw(screen)

        if game.dialog.visible:
            game.dialog.draw(screen)
            
        pygame.display.update()
        timer.tick(60)

if __name__ == "__main__":
    main()
