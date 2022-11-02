import cv2 as cv

img = cv.imread('borders.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
borders = cv.Canny(gray, 100, 200)

outlines, _ = cv.findContours(
    borders, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, outlines, -1, (0, 0, 255), 2)

txt = 'Outlines found:' + str(len(outlines))
print(txt)
cv.putText(img, txt, (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.7,
(255, 0, 0), 1)

cv.imshow('img', img)
cv.imshow('img_canny', borders)

cv.waitKey(0)
