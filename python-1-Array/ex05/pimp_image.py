import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the colors of the image by subtracting each pixel value from 255.
    """
    return 255 - array


def ft_red(array) -> np.ndarray:
    """
    Preserves the red channel and sets the green and blue channels to zero.
    """
    return array[..., [0, 1, 2]] * [1, 0, 0]


def ft_green(array) -> np.ndarray:
    """
    Preserves the green channel and sets the red and blue channels to zero.
    """
    green_array = np.copy(array)
    green_array[..., [0, 2]] -= green_array[..., [0, 2]]
    return green_array


def ft_blue(array) -> np.ndarray:
    """
    Preserves the blue channel and sets the red and green channels to zero.
    """
    blue_array = np.copy(array)
    blue_array[..., [0, 1]] = 0
    return blue_array


def ft_grey(array) -> np.ndarray:
    """
    Converts the image to grey using a weighted average of the RGB channels.
    """
    return np.dot(array[..., 0:3], [0.299, 0.587, 0.114]).astype(np.uint8)
