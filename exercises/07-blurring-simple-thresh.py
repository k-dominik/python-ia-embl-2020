import skimage
import matplotlib.pyplot as plt
# 'magic' to display plots in the jupyter notebook
%matplotlib inline 

image = skimage.io.imread('../data/07-noisy-shapes.tif', as_gray = True)

# the threshold
t = 0.9
mask = image < t

plt.figure()
plt.imshow(mask, cmap = 'gray')
