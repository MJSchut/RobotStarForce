import os

from src.world.tiles.tile import Tile
from src.managers.dirmanager import DirManager

class TileFactory:
    def __init__(self):
        self.tileDir = os.path.join(DirManager.instance().GRAPHICSDIR, "tiles")

    def make_empty_tile(self):
        ntile = Tile()
        ntile.passable = False
        ntile.sprite = os.path.join(self.tileDir, "s_Tile_Empty_.png")

        return ntile

    def make_grass_tile(self):
        ntile = Tile()
        ntile.passable = True
        ntile.sprite = os.path.join(self.tileDir, "s_Tile_Grass_.png")

        return ntile