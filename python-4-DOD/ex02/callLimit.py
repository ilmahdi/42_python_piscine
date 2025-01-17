from typing import Any


class TooManyCallsError(Exception):
    """Custom exception raised when a function is called too many times."""

    def __init__(self, func):
        """Initialize the exception with the offending function."""
        super().__init__(f"Error: {func} call too many times")
        self.func = func


def callLimit(limit: int):
    """Decorator factory to limit the number of calls to a function."""
    count = limit

    def callLimiter(function):
        """Decorator to track and limit calls to the given function."""
        calls = [0]

        def limit_function(*args: Any, **kwds: Any):
            """Limits the function execution based on the predefined count."""
            if calls[0] < count:
                function(*args, **kwds)
            else:
                print(TooManyCallsError(function))

            calls[0] += 1

        return limit_function

    return callLimiter
