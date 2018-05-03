class StateManager:
    """
    Functions for different game states.

    The game is always in a state (e.g. a menu state, or a play state). The statemanager functions
    as a finite state machine. An entry state must be given to initialize the state manager.
    """

    @property
    def currentState(self):
        return self._currentState

    @currentState.setter
    def currentState(self, newState):
        self.switch_states(newState)

    def __init__(self, entryState, renderbuffer):
        self.renderBuffer = renderbuffer
        self._currentState = entryState
        self._currentState.start(self.renderBuffer)

    def __str__(self):
        return str(type(self._currentState))

    def switch_states(self, newState):
        """
        Switch to a new game state.

        :param newState: New game state you want to enter, make sure it is called.
        :return: None
        """
        self._currentState = newState
        self._currentState.start(self.renderBuffer)

    def check_for_state(self, checkState):
        """
        :param checkState: Type of state to check for. e.g. am I in the PlayState right now?
        :return: bool, True if current state matches checkState, false if not.
        """
        if type(self._currentState) == checkState: return True
        else: return False