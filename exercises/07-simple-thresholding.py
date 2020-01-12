import numpy as np
import skimage
import matplotlib.pyplot as plt
# 'magic' to display plots in the jupyter notebook
%matplotlib inline 

# we want to look at grayscale histograms
def plot_histogram(image):
    
    histogram, bin_edges = np.histogram(image[mask], bins = 256, range = (0,1))
    plt.plot(bin_edges[:-1], histogram, color = 'k')
    
    plt.xlabel('Pixel value')
    plt.ylabel('Counts')
    plt.title('Grayscale Histogram')

image = skimage.io.imread('../data/07-shapes.tif', as_gray = True)

plt.figure()
plt.imshow(image, cmap = 'gray')

# YOUR CODE HERE
