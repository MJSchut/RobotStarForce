from src.world.tiles.tilemap import TileMap

from src.constants.gameconstants import TILEHEIGHT
from src.constants.gameconstants import TILEWIDTH

class World:
    @property
    def tiles(self):
        return self._tilemap.tiles

    @property
    def tilemap(self):
        return self._tilemap

    @property
    def worldWidth(self):
        return self._tilemap.worldWidth

    @property
    def worldHeight(self):
        return self._tilemap.worldHeight

    def __init__(self, worldWidth, worldHeight):
        self._tilemap = TileMap(worldWidth, worldHeight)

    def draw(self, renderbuffer):
        for x in range(self.worldWidth):
            for y in range(self.worldHeight):
                renderbuffer.blit(self.tiles[x,y].sprite, (x * TILEWIDTH,y * TILEHEIGHT))
