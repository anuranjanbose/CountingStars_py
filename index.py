from matplotlib import pyplot as plt

from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

import random

ind = random.randint(0,1)
print(ind)

example_file = glob.glob(r"img/*.png")[ind]
im = imread(example_file,as_gray=True)
plt.imshow(im, cmap = "gray")
plt.show()

blobs_log = blob_log(im, max_sigma = 30, num_sigma = 10, threshold = .1)

blobs_log[:,2] = blobs_log[:,2] * sqrt(2)

num_rows = len(blobs_log)

print("Number of stars counted:{} ".format(num_rows))



fig, ax = plt.subplots(1,1)
plt.imshow(im,cmap="gray")

for blob in blobs_log:
	y, x, r = blob
	c = plt.Circle((x,y), r+5, color="lime", linewidth=2, fill = False)
	ax.add_patch(c)
