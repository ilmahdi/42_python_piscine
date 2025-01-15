import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and return a truncated version based on the provided
    start and end indices.

    Args:
        family (List[List[Union[float, int]]]): A 2D list (array) of numbers.
        start (int): The starting index for slicing.
        end (int): The ending index for slicing.

    Returns:
        List[List[Union[float, int]]]: The truncated 2D list.
    """
    if (
        not isinstance(family, list)
        or not isinstance(start, int)
        or not isinstance(end, int)
    ):
        raise TypeError("Input must be a 2D list.")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("All elements in the input must be lists.")
    if len(set([len(row) for row in family])) != 1:
        raise ValueError("All sublists must have the same length.")

    family = np.array(family)
    rlen = family.shape[0]

    if start < -rlen or start >= rlen or end < -rlen or end > rlen:
        raise ValueError("Invalid sub array.")

    subarray = family[start:end]
    print(f"My shape is : {family.shape}")
    print(f"My new shape is : {subarray.shape}")
    return subarray.tolist()
