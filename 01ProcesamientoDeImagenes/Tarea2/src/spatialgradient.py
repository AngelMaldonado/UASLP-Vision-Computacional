from math import gamma
import cv2 as cv

img = cv.imread('../img/dog.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

dx, dy = cv.spatialGradient(img)
abs_grad_x = cv.convertScaleAbs(dx)
abs_grad_y = cv.convertScaleAbs(dy)

wx = 0.5
wy = 0.5
gam = 0
while True:
    dst = cv.addWeighted(abs_grad_x, wx, abs_grad_y, wy, gam)
    cv.imshow('Spatial Gradient', dst)

    print('wx:' + str(wx) + ' wy:' + str(wy) + ' gamma:' + str(gam))
    k = cv.waitKey(0)
    match k:
        case 49:
            wx = wx - 0.5
        case 50:
            wx = wx + 0.5
        case 51:
            wy = wy - 0.5
        case 52:
            wy = wy + 0.5
        case 53:
            gam = gam - 0.5
        case 54:
            gam = gam + 0.5
        case 120:
            break
