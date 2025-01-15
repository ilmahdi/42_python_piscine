import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path, print its shape, and return
    the pixel content in RGB format.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: A NumPy array representing the image in RGB format.
    """
    try:
        image = np.array(Image.open(path))
        return image
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{path}' does not exist.")
    except Exception as e:
        raise Exception(f"Error loading image: {e}")
