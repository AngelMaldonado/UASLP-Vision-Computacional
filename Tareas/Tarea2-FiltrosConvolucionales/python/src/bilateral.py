import cv2 as cv

img = cv.imread('../img/dog.jpg')

d = 9
sigmaColor = sigmaSpace = 75

while True:
    dst = cv.bilateralFilter(img, d, sigmaColor, sigmaSpace)
    cv.imshow('Bilateral filter', dst)

    print('d' + str(d) + 'sigC' + str(sigmaColor) + 'sigS' + str(sigmaSpace))
    k = cv.waitKey(0)
    match k:
        case 49:
            d = d - 1
        case 50:
            d = d + 1
        case 51:
            sigmaColor = sigmaColor - 1
        case 52:
            sigmaColor = sigmaColor + 1
        case 53:
            sigmaSpace = sigmaSpace - 1
        case 54:
            sigmaSpace = sigmaSpace + 1
        case 120:
            break
