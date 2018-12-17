import pygame
from pygame import *
from settings import *
from entities import *
from misc import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE.size)
    timer = pygame.time.Clock()

    level = Map("maps/empty.txt")

    levelWidth = level.width
    levelHeight = level.height

    player = Player((TILESIZE, levelHeight - 2 * TILESIZE))

    print("LEVEL height: " + str(levelHeight))
    print("Screen height: " + str(SCREENSIZE.height))
    entities = CameraLayeredUpdates(player, pygame.Rect(0, 0, levelWidth, levelHeight))

    # wall sprite group.
    walls = pygame.sprite.Group()

    # path sprite group.
    paths = pygame.sprite.Group()

    # build level.
    x = y = 0
    for row in level.data:
        for col in row:
            if col == "W":
                # its in both walls sprite group and entities sprite group.
                Wall((x, y), walls, entities)

            x += TILESIZE
        y += TILESIZE
        x = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        entities.update()

        screen.fill((0, 0, 0))
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)


if __name__ == "__main__":
    main()
