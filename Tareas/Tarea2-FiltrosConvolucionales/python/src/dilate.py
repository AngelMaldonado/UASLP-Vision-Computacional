import cv2 as cv

img = cv.imread('../img/dog.jpg')

# shape = {MORPH_RECT, MORPH_CROSS, MORPH_ELLIPSE}
shape = cv.MORPH_RECT
ksize = 5

while True:
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (ksize, ksize))

    dst = cv.dilate(img, kernel)
    cv.imshow('Dilate filter', dst)

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
