import cv2 as cv

img = cv.imread('../img/dog.jpg')

ksize = 3
sigma = 0

while True:
    dst = cv.GaussianBlur(img, (ksize, ksize), sigma, sigma)
    cv.imshow('Gaussian filter', dst)

    print('Kernel size: ' + str(ksize) + ', Sigma: ' + str(sigma))
    k = cv.waitKey(0)
    match k:
        case 49:
            ksize = ksize - 2
        case 50:
            ksize = ksize + 2
        case 51:
            sigma = sigma - 1
        case 52:
            sigma = sigma + 1
        case 120:
            break
