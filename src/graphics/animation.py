class Animation:
    """
    Holds and manipulates a list of sprites.

    The animation list is called frames.
    """
    
    @property
    def frames(self):
        return self._frames

    @frames.setter
    def frames(self, **kwargs):
        raise ValueError("Cannot set frame directly, use add_frame or reset_frames instead")

    def __init__(self):
        self._frames = []

    def __len__(self):
        return len(self._frames)

    def add_frame(self, image):
        """
        Add one frame to an animation.
        :param image: path to image to add to the animation.
        :return: None
        """
        self._frames.append(image)

