import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')

kernel3x3 = np.ones((3, 3), np.float32)/9.0
kernel5x5 = np.ones((5, 5), np.float32)/25.0

salida3 = cv.filter2D(img, -1, kernel3x3)
salida5 = cv.filter2D(img, -1, kernel5x5)
# aplicando otros filtros
filtroGausiano = cv.GaussianBlur(img, (5, 5), 0)
# filtra mediana
filtraMediana = cv.medianBlur(img, 5)

cv.imshow('filtroGausiano', filtroGausiano)
cv.imshow('filtraMediana', filtraMediana)

cv.imshow('original', img)
cv.imshow('salida3', salida3)
cv.imshow('salida5', salida5)

cv.waitKey(0)
