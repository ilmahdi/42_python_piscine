class Calculator:
    """A class to perform some arithmetic operations on a vector."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the dot product of two vectors."""
        print(f"Dot product is: {sum(x * y for x, y in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the element-wise addition of two vectors."""
        print(f"Add Vector is: {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate and print the element-wise subtraction of two vectors."""
        print(f"Sous Vector is: {[float(x - y) for x, y in zip(V1, V2)]}")
