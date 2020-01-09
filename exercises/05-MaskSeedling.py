
import skimage
import numpy as np
from skimage.viewer import ImageViewer

# the image to mask
image = skimage.io.imread('../data/seedling.tif', as_gray = True)

# display the image and interactively
# determine ROI coordinates
viewer = ImageViewer(image)
viewer.show()

# YOUR CODE HERE
mask = ____
