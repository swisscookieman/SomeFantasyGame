import climage
from PIL import Image
import numpy as np
import os

dir = "assets/items/"
allfiles = os.listdir(dir)

for image_path in allfiles:
    image_path = dir+image_path
    if os.path.isfile(image_path):
        img = Image.open(image_path).convert('RGB').resize((16, 16))
        arr = np.array(img)
        output = climage.convert_array(arr, is_unicode=True)
        print(output)
