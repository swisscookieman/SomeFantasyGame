from PIL import Image
assets_dir = "assets/items/equipment"

def print_image(image_path):
    try:
        # Open, resize image
        image = Image.open(image_path)
        image = image.resize((16, 16))
        width, height = image.size

        # Iterate over each pixel and print the corresponding character with color
        for y in range(height):
            for x in range(width):
                r, g, b, _ = image.getpixel((x, y))
                color_code = f"\033[38;2;{r};{g};{b}m" # Convert RGB to ANSI color codes
                print(color_code + "██", end="")

            # Move to the next line after each row is printed
            print("\033[0m")  # Reset color to default at the end of each row

    except Exception as e:
        print("Error:", e)

def images_list(initial_dir):
    image_paths = []
    for image in initial_dir:
        image_paths.append(image)
    return image_paths

image_paths = images_list(assets_dir)
print(image_paths)
# for image in image_paths:
#     print_image(image)
