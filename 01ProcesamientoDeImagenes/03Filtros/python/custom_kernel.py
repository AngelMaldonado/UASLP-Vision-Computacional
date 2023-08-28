import numpy as np
import cv2 as cv

# read image
img = cv.imread('sample.jpg')

# kernel sensitive to horizontal lines
kernel = np.array([
    [-1.0, -1.0],
    [2.0, 2.0],
    [-1.0, -1.0]
])

kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)

# filter the source image
img_filtered = cv.filter2D(img, -1, kernel)

# show results
cv.imshow('original', img)
cv.imshow('filtered', img_filtered)

cv.waitKey(0)