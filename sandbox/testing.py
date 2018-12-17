import pygame

tilesize = 16

windowWidth = 160
windowHeight = 160

gamewindow = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("testingbox")
map = pygame.image.load('img/testmap.png')
mapwidth = 320
mapheight = 320


pygame.init()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.moveup = 0
        self.movedown = 0
        self.moveleft = 0
        self.moveright = 0
        self.move = False

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (80, 80, self.width, self.height))

run = True

char = player(80, 80, 16, 16)

while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        run = False
        break

    if char.move:
        if char.moveleft > 0:
            char.x -= char.vel
            char.moveleft -= 1
            if char.moveleft == 0:
                char.move = False
        if char.moveright > 0:
            char.x += char.vel
            char.moveright -= 1
            if char.moveright == 0:
                char.move = False
        if char.moveup > 0:
            char.y -= char.vel
            char.moveup -= 1
            if char.moveup == 0:
                char.move = False
        if char.movedown > 0:
            char.y += char.vel
            char.movedown -= 1
            if char.movedown == 0:
                char.move = False
        print(char.x, char.y)
    else:
        if keys[pygame.K_LEFT]:
            char.x -= char.vel
            char.moveleft = 3
            char.move = True
        elif keys[pygame.K_RIGHT]:
            char.x += char.vel
            char.moveright = 3
            char.move = True
        elif keys[pygame.K_UP]:
            char.y -= char.vel
            char.moveup = 3
            char.move = True
        elif keys[pygame.K_DOWN]:
            char.y += char.vel
            char.movedown = 3
            char.move = True
            print(char.x, char.y)

    gamewindow.blit(map, (-char.x, -char.y))

    char.draw(gamewindow)
    pygame.display.update()

