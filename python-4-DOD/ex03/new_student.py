import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character lowercase ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with a name, surname, login, and ID."""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Initializes the login and ID after the object is created."""
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
        self.id = generate_id()
