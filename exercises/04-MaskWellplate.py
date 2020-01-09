"""
 * Program to start the wellplate exercise

   Given the well center coordinates, 
   create a mask with a circular region 
   of interest for each well.
"""
import skimage
import numpy as np
import random
from skimage.viewer import ImageViewer
import pandas as pd

# the center coordinates
df = pd.read_table('../data/wellplate_centers.csv', sep = ',', header = 0)

# the image to mask
image = skimage.io.imread('../data/wellplate.tif')

# display the image
viewer = ImageViewer(image)
viewer.show()

# YOUR CODE HERE
