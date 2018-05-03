class Tile:
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
        self._sprite = nsprite

    def __init__(self, passable = True):
        self._passable = passable

