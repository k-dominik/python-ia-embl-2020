
import skimage
import numpy as np
import random
from skimage.viewer import ImageViewer
import pandas as pd

# the well center coordinates
df = pd.read_table('../data/wellplate_centers.csv', sep = ',', header = 0)

# the image to mask
image = skimage.io.imread('../data/wellplate.tif')

# display the image
viewer = ImageViewer(image)
viewer.show()

# YOUR CODE HERE
