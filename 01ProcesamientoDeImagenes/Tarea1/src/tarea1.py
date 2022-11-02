import cv2 as cv

img = cv.imread('dog.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv.getRotationMatrix2D((cX, cY), 60, 1.0)
img = cv.warpAffine(img, M, (w, h))
cv.imshow('B&W + 60deg', img)
k = cv.waitKey(0)
