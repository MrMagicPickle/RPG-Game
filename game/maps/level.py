from mapClass import *
import pygame

#-- Camera.
sys.path.append("camera")
from scrollingCamera import *

from wall import *
from testObject import *

#-- Entities.
class Level():
    def __init__(self, name):
        level = TiledMap(name)
        self.data = level.data
        self.width = level.width
        self.height = level.height
        self.walls = pygame.sprite.Group()
        self.interactables = pygame.sprite.Group()
        self.entities = CameraLayeredUpdates(pygame.Rect(0, 0, level.width, level.height))
        self.background = level.bg
        self.buildLevel()

    def loadObjectData(self):
        pass

    def buildLevel(self):
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
        for ob in self.data.objects:
            if ob.type == "Player":
                self.player = ob
            if ob.type == "Wall":
                Wall((ob.x, ob.y), ob.width, ob.height, self.walls, self.entities)
            if ob.type == "Object":
                # maybe building objects can be split also idk
                TestObject(objectList[objectCount], pygame.Color(objectColors[objectCount]), (ob.x, ob.y),
                           objectDesc[objectCount], self.interactables, self.entities)
                objectCount += 1

    def playerStartPoint(self, player):
        player.rect.left = self.player.x
        player.rect.top = self.player.y