from S1E9 import Character


class Baratheon(Character):
    """
    Class representing the Baratheon family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Baratheon character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Return a string representation of the Baratheon character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return a formal string representation of the Baratheon character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Change the health state of the Lannister family from alive to dead.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Class representing the Lannister family.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Lannister character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Return a string representation of the Lannister character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return a formal string representation of the Lannister character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """
        Create a Lannister character.
        """
        return cls(first_name, is_alive)

    def die(self):
        """
        Change the health state of the Lannister family from alive to dead.
        """
        self.is_alive = False
