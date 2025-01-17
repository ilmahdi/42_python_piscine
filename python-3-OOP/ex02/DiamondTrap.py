from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing King Joffrey Baratheon.
    """

    def __init__(self, first_name, is_alive=True):
        """Initialize a King character."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Setter for the eyes attribute."""
        self.eyes = color

    def set_hairs(self, color):
        """Setter for the hairs attribute."""
        self.hairs = color

    def get_eyes(self):
        """Get the eyes attribute."""
        return self.eyes

    def get_hairs(self):
        """Get the hairs attribute."""
        return self.hairs
