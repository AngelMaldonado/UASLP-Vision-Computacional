import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)

cv.imshow('img', img)
cv.imshow('erode', erosion)
cv.imshow('dilate', dilation)

cv.waitKey(0)
