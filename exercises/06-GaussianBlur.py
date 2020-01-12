import skimage
from skimage import filters

import matplotlib.pyplot as plt
# 'magic' to display plots in the jupyter notebook
%matplotlib inline 

original = skimage.io.imread('../fig/06-gaussian-original.png')

plt.figure()
plt.imshow(original)

# apply the filter
# YOUR CODE HERE 
