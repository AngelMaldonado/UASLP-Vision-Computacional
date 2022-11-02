import cv2 as cv
import numpy as np

img = cv.imread('sample.jpg')

kernel = np.ones((5, 5), np.uint8)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


cv.imshow('original', img)
cv.imshow('opening', opening)
cv.imshow('closing', closing)
cv.imshow('gradient', gradient)
cv.imshow('tophat', tophat)
cv.imshow('blackhat', blackhat)

cv.waitKey(0)
