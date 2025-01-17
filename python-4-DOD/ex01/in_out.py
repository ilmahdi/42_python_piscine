def square(x: int | float) -> int | float:
    """Returns the square of the given number."""
    return x**2


def pow(x: int | float) -> int | float:
    """Returns the number raised to the power of itself."""
    return x**x


def outer(x: int | float, function) -> object:
    """
    Returns an inner function that applies the given function to `x`
    and updates the value on each call.
    """
    count = [x]

    def inner() -> float:
        """Applies the provided function to the stored value and returns it."""
        count[0] = function(count[0])
        return count[0]

    return inner
