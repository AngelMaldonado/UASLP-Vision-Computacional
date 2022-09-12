import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dog.jpg', 0)
#img = np.zeros((200, 200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
# b, g, r = cv.split(img)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# cv.imshow('img', img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)

# ravel() returns a flat 1D array
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
#plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
