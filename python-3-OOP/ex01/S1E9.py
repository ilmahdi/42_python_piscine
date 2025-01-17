from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character with a first name and health state.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Change the health state of the character from alive to dead.
        """
        pass


class Stark(Character):
    """
    Class representing a Stark character.
    """

    def die(self):
        """
        Change the health state of the Stark character from alive to dead.
        """
        self.is_alive = False
