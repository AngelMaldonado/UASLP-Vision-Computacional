import cv2 as cv
import sys

img = cv.imread('img/01Spiderman.jpg')

if img is None:
    sys.exit('Could not read the image')

cv.imshow('Display window', img)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite('img/01Spiderman.png', img)
