import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


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
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.show()
    except Exception as e:
        raise Exception(f"Error displaying image: {e}")


def main():
    try:
        image_array = ft_load("animal.jpeg")
        zoomed_array = image_array[100:500, 450:850, 0:1]

        print(image_array)
        print(f"New shape after slicing: {zoomed_array.shape}")
        print(zoomed_array)

        display_image(zoomed_array, "Zoomed Image")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
