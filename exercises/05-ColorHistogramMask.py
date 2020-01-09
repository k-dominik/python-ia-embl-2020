import skimage.draw
import skimage.io
import skimage.viewer
import numpy as np
from matplotlib import pyplot as plt

# read original image, in full color, based on command
# line argument
image = skimage.io.imread('../data/plate-01.tif')

# display the original image
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# create a circular mask to select the 7th well in the first row
# WRITE YOUR CODE HERE

# make a copy of the image, call it masked_image, and
# use np.logical_not() and indexing to apply the mask to it
# WRITE YOUR CODE HERE

# plot the masked_image, to verify the
# validity of your mask
# WRITE YOUR CODE HERE

# dictionary to select colors of each channel 
chan_to_ind = {'red' : 0, 'green' : 1, 'blue' : 2}

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for channel_name in chan_to_ind:
    channel_ind = chan_to_ind[channel_name]
    # change this to use your circular mask to apply the histogram
    # operation to the 7th well of the first row
    # MODIFY CODE HERE
    histogram, bin_edges = np.histogram(image[:, :, channel_ind],
                                        bins=256, range=(0, 256))

    plt.plot(bin_edges[0:-1], histogram, color= channel_name)

plt.xlabel("color value")
plt.ylabel("pixel count")
