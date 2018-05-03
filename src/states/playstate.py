import pygame

from src.constants.gameconstants import WORLDWIDTH
from src.constants.gameconstants import WORLDHEIGHT

from src.states.basestate import BaseState

from src.world.world import World

class PlayState(BaseState):
    def start(self, renderbuffer):
        self.world = World(WORLDWIDTH, WORLDHEIGHT)
        self.renderbuffer = renderbuffer

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def draw(self):
        self.world.draw(self.renderbuffer)
