from PIL import Image


def print_image(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Resize the image to fit the terminal
        image = image.resize((16, 16))

        # Get the width and height of the resized image
        width, height = image.size

        # Iterate over each pixel and print the corresponding character with color
        for y in range(height):
            for x in range(width):
                # Get the RGB values of the pixel
                r, g, b, _ = image.getpixel((x, y))

                # Convert RGB to ANSI color codes
                color_code = f"\033[38;2;{r};{g};{b}m"

                # Print a colored character
                print(color_code + "██", end="")

            # Move to the next line after each row is printed
            print("\033[0m")  # Reset color to default at the end of each row

    except Exception as e:
        print("Error:", e)


# We need to better this by making a function to do this vv
image_paths = ["assets/items/archer_bow.png","assets/items/assasin_dagger.png","assets/items/mage_cape.png","assets/items/mage_staff.png","assets/items/mercenary_armor.png","assets/items/mercenary_axe.png","assets/items/warrior_chestplate.png","assets/items/warrior_sword.png"]
for image in image_paths:
    print_image(image)
