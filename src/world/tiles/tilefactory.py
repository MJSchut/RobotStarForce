from src.world.tiles.tile import Tile

class TileFactory:
    def __init__(self):
        pass

    def make_empty_tile(self):
        ntile = Tile()
        ntile.passable = False

        return ntile

    def make_grass_tile(self):
        ntile = Tile()
        ntile.passable = True

        return ntile