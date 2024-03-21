from PIL import Image


def print_image(image_path, print_mode):
    try:
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

            print("\033[0m")

    except Exception as e:
        print("Error:", e)


# We need to better this by making a function to do this vv
image_paths = ["assets/items/archer_bow.png","assets/items/assasin_dagger.png","assets/items/mage_cape.png","assets/items/mage_staff.png","assets/items/mercenary_armor.png","assets/items/mercenary_axe.png","assets/items/warrior_chestplate.png","assets/items/warrior_sword.png"]
for image in image_paths:
    print_image(image)
