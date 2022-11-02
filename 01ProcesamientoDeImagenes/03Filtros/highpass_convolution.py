import numpy as np
import cv2 as cv

# read image
img = cv.imread('sample.jpg')

# edge detection filter/kernel
kernel = np.array([
    [0.0, -1.0, 0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0, 0.0]
])

kernel_color = np.array([
    [0.0, -1.0, 0.0],
    [-1.0, 5.0, -1.0],
    [0.0, -1.0, 0.0]
])

kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)
kernel_color = kernel_color / \
    (np.sum(kernel_color) if np.sum(kernel_color) != 0 else 1)

# filter the source image
img_filtered = cv.filter2D(img, -1, kernel)
img_filtered_color = cv.filter2D(img, -1, kernel_color)

# show results
cv.imshow('original', img)
cv.imshow('filtered', img_filtered)
cv.imshow('filtered_color', img_filtered_color)

cv.waitKey(0)
