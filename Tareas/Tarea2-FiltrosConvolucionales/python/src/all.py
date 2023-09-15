"""
Universidad Autónoma de San Luis Potosí
Facultad de Ingeniería
Visión Computacional

Autor: Angel de Jesús Maldonado Juárez
Fecha de Creación: 13 de septiembre de 2023

Descripción: Uso de varios filtros convolucionales
con opencv.
"""

## Importación de librerías
import cv2 as cv

## Lectura de la imgen
img = cv.imread('../img/astronaut.jpg')

## Aplicación del filtro Bilateral
img_bilateral = cv.bilateralFilter(img, 9, 75, 75)

## Aplicación del filtro Blur
img_blur = cv.blur(img, (9, 9))

## Aplicación del filtro Dilate
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
img_dilate = cv.dilate(img, kernel)

## Aplicación del filtro Erode
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
img_erode = cv.erode(img, kernel)

## Aplicación del filtro GaussianBlur
img_gaussian = cv.GaussianBlur(img, (9, 9), 0)

## Aplicación del filtro MedianBlur
img_median = cv.medianBlur(img, 9)

## Aplicación del filtro SpatialGradient
dx, dy = cv.spatialGradient(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
abs_grad_x = cv.convertScaleAbs(dx)
abs_grad_y = cv.convertScaleAbs(dy)
img_spatial = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

## Guardado de las imagenes filtradas
cv.imwrite('../img/astronaut_bilateral.jpg', img_bilateral)
cv.imwrite('../img/astronaut_blur.jpg', img_blur)
cv.imwrite('../img/astronaut_dilate.jpg', img_dilate)
cv.imwrite('../img/astronaut_erode.jpg', img_erode)
cv.imwrite('../img/astronaut_gaussian.jpg', img_gaussian)
cv.imwrite('../img/astronaut_median.jpg', img_median)
cv.imwrite('../img/astronaut_spatial.jpg', img_spatial)