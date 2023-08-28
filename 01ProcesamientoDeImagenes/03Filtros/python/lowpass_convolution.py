# Source: https://pythonexamples.org/python-opencv-image-filter-convolution-cv2-filter2d/
import numpy as np
import cv2 as cv

# read image
img = cv.imread('dog.jpg')

# prepare the 5x5 shaped filter
kernel = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
])

kernel = kernel/sum(kernel)

# filter the source image
img_filtered = cv.filter2D(img, -1, kernel)

# show results
cv.imshow('original', img)
cv.imshow('filtered', img_filtered)

cv.waitKey(0)
