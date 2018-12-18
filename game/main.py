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


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    timer = pygame.time.Clock()

    level = Map("maps/empty.txt")

    levelWidth = level.width
    levelHeight = level.height

    player = Player((TILE_SIZE, levelHeight - 2 * TILE_SIZE))

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
    a = TestObject("a", pygame.Color("#0000FF"), (320, 320), interactables, entities)
    b = TestObject("b", pygame.Color("#00FFFF"), (352, 320), interactables, entities)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        entities.update()
        game.dialog.update()
        screen.fill((0, 0, 0))
        entities.draw(screen)

        if not game.dialog.hide:
            game.dialog.hasControl = True
            game.dialog.draw(screen)
            
        pygame.display.update()
        timer.tick(60)


if __name__ == "__main__":
    main()
