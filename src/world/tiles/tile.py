import pygame

from src.constants.gameconstants import TILEWIDTH
from src.constants.gameconstants import TILEHEIGHT

class Tile(pygame.sprite.Sprite):
    @property
    def passable(self):
        return self._passable

    @passable.setter
    def passable(self, boolPassable):
        if boolPassable == 0: boolPassable = True
        elif boolPassable == 1: boolPassable = False
        if type(boolPassable) is not type(True): raise ValueError("the passable atribute must be set to a bool")

        self._passable = boolPassable

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, nsprite):
        if type(nsprite) == type("string"):
            self._sprite = pygame.image.load(nsprite)
        else: self._sprite = nsprite

    def __init__(self, passable = True):
        pygame.sprite.Sprite.__init__(self)
        self._passable = passable
        self._sprite = pygame.Surface((TILEWIDTH, TILEHEIGHT))