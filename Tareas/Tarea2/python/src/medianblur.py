import cv2 as cv

img = cv.imread('../img/dog.jpg')

ksize = 9

while True:
    dst = cv.medianBlur(img, ksize)
    cv.imshow('Median filter', dst)

    print('Kernel size: ' + str(ksize))
    k = cv.waitKey(0)
    match k:
        case 49:
            ksize = ksize - 2
        case 50:
            ksize = ksize + 2
        case 120:
            break