import skimage.color
import skimage.filters
import skimage.io
import skimage.measure
import skimage.viewer

# get filename, sigma, and threshold value from command line
filename = "../data/08-shapes.tif"
sigma = 2.0
t = 0.8

# read and display the original image
image = skimage.io.imread(fname=filename, as_gray=True)

# blur and grayscale before thresholding
blur = skimage.filters.gaussian(image, sigma=sigma)

# perform inverse binary thresholding
mask = blur < t

# Perform CCA on the mask
labeled_image = skimage.measure.label(mask, connectivity=2)
