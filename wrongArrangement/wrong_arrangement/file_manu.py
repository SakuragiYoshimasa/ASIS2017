#coding: utf-8

import numpy as np
from PIL import Image

img1 = Image.open('image1.png').load()
print(img1)
img1array = np.asarray(img1)

print(img1array)
