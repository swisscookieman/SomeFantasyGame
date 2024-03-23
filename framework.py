# Imports
from PIL import Image
import os

# Not framework yet, more like bordel for now

# Variables init
assets_dir = "assets/items/equipment/"

def print_image(image_path, print_mode="no_bg", color_r="", color_g="", color_b=""):
    try:
        # Open, resize image
        image = Image.open(image_path)
        image = image.resize((16, 16))
        width, height = image.size

        for y in range(height):
            for x in range(width):
                r, g, b, _ = image.getpixel((x, y))

                # Print with a checkboard behing
                if print_mode == "check":
                    if r == g == b == 0:
                        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                            print(f"\033[38;2;255;255;255m" + "██", end="")
                        if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
                            print(f"\033[38;2;180;180;180m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                # Print with no bg
                if print_mode == "no_bg":
                    if r == g == b == 0:
                        print("  ", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                # Print with white bg
                if print_mode == "white":
                    if r == g == b == 0:
                        print(f"\033[38;2;255;255;255m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

                if print_mode == "custom":
                    if r == g == b == 0:
                        print(
                            f"\033[38;2;{color_r};{color_g};{color_b}m" + "██", end="")
                    else:
                        color_code = f"\033[38;2;{r};{g};{b}m"
                        print(color_code + "██", end="")

            print("\033[0m")

    except Exception as e:
        print("Error:", e)

    print("")

def list_images(directory):
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            image_paths.append(str(os.path.join(root, file)))
    return image_paths