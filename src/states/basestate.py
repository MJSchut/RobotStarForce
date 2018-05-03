class BaseState:
    """
    Architecture for game states.
    """

    def start(self):
        # called once before first update call
        pass

    def update(self):
        # put game logic here
        pass
    
    def draw(self):
        # put game rendering here
        pass