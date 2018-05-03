import numpy as np

from src.world.tiles.tilefactory import TileFactory
from src.world.tiles.tile import Tile

class TileMap:
    @property
    def tiles(self):
        return self._tiles

    @property
    def worldWidth(self):
        return self._worldWidth

    @property
    def worldHeight(self):
        return self._worldHeight

    def __init__(self, worldWidth, worldHeight):
        self._worldWidth = worldWidth
        self._worldHeight = worldHeight
        self._tiles = np.zeros((worldWidth, worldHeight))

        self._tileFactory = TileFactory()

        self._init_tiles()

    def _init_tiles(self):
        self._tiles = self._tiles.astype(Tile)
        for x in range(self._worldWidth):
            for y in range(self._worldHeight):
                self._tiles[x, y] = self._tileFactory.make_empty_tile()