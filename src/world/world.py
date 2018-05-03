from src.world.tiles.tilemap import TileMap

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

