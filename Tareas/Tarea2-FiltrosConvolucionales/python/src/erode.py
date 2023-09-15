import cv2 as cv
import numpy as np

img = cv.imread('../img/dog.jpg')

shape = cv.MORPH_RECT
ksize = 9

while True:
    kernel = cv.getStructuringElement(shape, (ksize, ksize))

    dst = cv.erode(img, kernel)
    cv.imshow('Erode filter', dst)

    print('Kernel size: ' + str(ksize) + ', Shape: ' + str(shape))
    k = cv.waitKey(0)
    match k:
        case 49:
            shape = cv.MORPH_RECT
        case 50:
            shape = cv.MORPH_CROSS
        case 51:
            shape = cv.MORPH_ELLIPSE
        case 52:
            ksize = ksize - 1
        case 53:
            ksize = ksize + 1
        case 120:
            break
