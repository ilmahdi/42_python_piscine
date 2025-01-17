class Calculator:
    """A class to perform basic arithmetic operations on a vector."""

    def __init__(self, vector) -> None:
        """Initialize the Calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector."""
        self.vector = [i + object for i in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar."""
        self.vector = [i * object for i in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector."""
        self.vector = [i - object for i in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar."""
        if object == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [i / object for i in self.vector]
        print(self.vector)
