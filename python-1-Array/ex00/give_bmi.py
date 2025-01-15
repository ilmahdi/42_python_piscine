import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate BMI from height and weight lists.

    Args:
        height (list[Union[int, float]]): List of heights in meters.
        weight (list[Union[int, float]]): List of weights in kilograms.

    Returns:
        list[int | float]: List of BMI values.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    for i, (h, w) in enumerate(zip(height, weight)):
        if not isinstance(h, (int, float)):
            raise TypeError(
                f"Height at index {i} must be int or float. Got {type(h)}."
            )
        if not isinstance(w, (int, float)):
            raise TypeError(
                f"Weight at index {i} must be int or float. Got {type(w)}."
            )
    height = np.array(height)
    weight = np.array(weight)
    return (weight / height**2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI value in the list exceeds the given limit.

    Args:
        bmi (List[Union[int, float]]): List of BMI values.
        limit (int): The threshold value to compare against.

    Returns:
        List[bool]: A list of booleans indicating whether each BMI
        value exceeds the limit.
    """
    if not isinstance(bmi, list):
        raise TypeError("Bmi must be a list of int or float.")
    for i, value in enumerate(bmi):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Bmi at index {i} must be int or float. Got {type(value)}."
            )

    if not isinstance(limit, int):
        raise TypeError("Limit must be an int.")
    bmi = np.array(bmi)
    return (bmi > limit).tolist()
