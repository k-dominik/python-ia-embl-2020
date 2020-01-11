import skimage.io
import skimage.viewer

# load and display original image
image = skimage.io.imread(fname="../data/roots.tif")
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# extract, display, and save sub-image
# WRITE YOUR CODE TO SELECT THE SUBIMAGE NAME clip HERE:

# WRITE YOUR CODE TO SAVE clip HERE
