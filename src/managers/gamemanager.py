
import pygame
import sys

from src.constants.displayconstants import WINDOW_WIDTH
from src.constants.displayconstants import WINDOW_HEIGHT
from src.constants.displayconstants import SCREEN_WIDTH
from src.constants.displayconstants import SCREEN_HEIGHT

from src.managers.statemanager import StateManager
from src.states.playstate import PlayState

class GameManager:
    """
    Functions for overarching game management.

    This class performs tasks that are outstide of the game scope. It does stuff like game initialization,
    by initializing pygame, etc. and initializing the other managers such as the state manager.

    When it is done doing these things it initializes the game loop as defined in the current state of the
    state manager.
    """

    def __init__(self):
        print ("Game manager started")
        
        self._initialize_pygame()
        self._initialize_global_variables()
        self._start_game_loop()

    def _initialize_pygame(self):
        print ("Initializing pygame...")

        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.render_buffer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        print("\t ...initialized.")

    def _initialize_global_variables(self):
        print("Initializing global variables...")
        self.stateManager = StateManager(PlayState())
        print("\t ...initialized.")

    def _start_game_loop(self):
        print("Entering game loop...")
                    
        while self.stateManager.currentState is not None:
            self.stateManager.currentState.draw()
            gameended = self.stateManager.currentState.update()

            if gameended:
                break

        self.quit_game()
        
    def quit_game(self):
        """
        Call to exit game and make sure everything closes down properly.
        :return: None
        """
        pygame.quit()
        sys.exit(0)