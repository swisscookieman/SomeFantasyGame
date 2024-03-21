import climage
from PIL import Image
import numpy as np
# converts the image to print in terminal
# inform of ANSI Escape codes
image_path = "assets/items/iron_sword.png"

img = Image.open(image_path).convert('RGB').resize((16, 16))
arr = np.array(img)
output = climage.convert_array(arr, is_unicode=True)
# prints output on console.
print(output)
