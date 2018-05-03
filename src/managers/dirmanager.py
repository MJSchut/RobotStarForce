import os
from src.util.singleton import Singleton

@Singleton
class DirManager:
    def __init__(self):
        self.SRCDIR = os.path.split(os.path.dirname(__file__))[0]
        self.ROOTDIR = os.path.split(self.SRCDIR)[0]
        self.ASSETDIR = os.path.join(self.ROOTDIR, "assets")
        self.GRAPHICSDIR = os.path.join(self.ASSETDIR, "graphics")
