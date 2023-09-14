"""
Universidad Autónoma de San Luis Potosí
Facultad de Ingeniería
Visión Computacional

Autor: Angel de Jesús Maldonado Juárez
Fecha de Creación: 11 de septiembre de 2023

Descripción:
Transformación de una imgen a escala de grises, y espacio de colores
YCrCb
"""

## Importación de librerías
import cv2 as cv

## Lectura de la imgen
img = cv.imread('../img/original.jpg')
## Transformación a escala de grises
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
## Guardado de la imagen
cv.imwrite('../img/grayscale.jpg', img_gray)
## Ecualización de la imagen en escala de grises
img_gray_eq = cv.equalizeHist(img_gray)
## Guardado de la imagen ecualizada
cv.imwrite('../img/grayscale_eq.jpg', img_gray_eq)

## Transformación a espacio de colores YCrCb
img_YCrCb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
## Guardado de la imagen
cv.imwrite('../img/YCrCb.jpg', img_YCrCb)
## Ecualización de la imagen en el componente Y
img_YCrCb[:,:,0] = cv.equalizeHist(img_YCrCb[:,:,0])
## Transformación a espacio de colores BGR
img_YCrCb_eq = cv.cvtColor(img_YCrCb, cv.COLOR_YCrCb2BGR)
## Guardado de la imagen ecualizada
cv.imwrite('../img/YCrCb_eq.jpg', img_YCrCb_eq)
