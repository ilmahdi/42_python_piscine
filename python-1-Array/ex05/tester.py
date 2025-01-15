import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def display_image(image_array: np.ndarray, title: str):
    """
    Display the image using Matplotlib.

    Args:
        image_array (np.ndarray): The image as a NumPy array.
        title (str): The title of the image.
    """
    try:
        plt.imshow(image_array, cmap="gray")
        plt.title(title)
        plt.axis("off")
        plt.show()
    except Exception as e:
        raise Exception(f"Error displaying image: {e}")


def main():
    try:
        image = ft_load("landscape.jpg")
        print("The shape of image is:", image.shape)
        print(image)

        display_image(image, "Original Image")
        display_image(ft_invert(image), "Invert Image")
        display_image(ft_red(image), "Red Image")
        display_image(ft_green(image), "Green Image")
        display_image(ft_blue(image), "Blue Image")
        display_image(ft_grey(image), "Grey Image")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
