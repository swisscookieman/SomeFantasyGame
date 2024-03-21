import json
from PIL import Image

# Define a function to convert an image to ASCII
def image_to_ascii(image_path, width=80, height=40):
    # Open the image and resize it
    img = Image.open(image_path).resize((width, height), Image.ANTIALIAS)
    img = img.convert('L') # Convert to grayscale

    # Define the ASCII characters to use for each brightness level
    ascii_chars = "@%#*+=-:. "

    # Convert the image to ASCII
    ascii_str = ""
    for y in range(height):
        for x in range(width):
            pixel_value = img.getpixel((x, y))
            ascii_str += ascii_chars[pixel_value // 32] # Map pixel value to ASCII character
        ascii_str += "\n"

    return ascii_str

# Define a function to generate the JSON file
def generate_textsprites_json(image_paths, output_path):
    textsprites = {}

    for image_path in image_paths:
        # Extract the file name without extension
        file_name = image_path.split('/')[-1].split('.')[0]
        # Convert the image to ASCII
        ascii_str = image_to_ascii(image_path)
        # Add the ASCII representation to the dictionary
        textsprites[file_name] = ascii_str

    # Serialize the dictionary to a JSON formatted string
    json_str = json.dumps(textsprites, indent=4)

    # Write the JSON string to a file
    with open(output_path, 'w') as f:
        f.write(json_str)

# Example usage:
image_paths = ['assets/items/mercenary_armor.png', 'assets/items/mercenary_axe.png'] # List of image```

generate_textsprites_json(image_paths,"assets/textsprites.json")