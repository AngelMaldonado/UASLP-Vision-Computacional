import numpy as np
import cv2 as cv

img = cv.imread('dog.jpg')

Nf = 512
Nc = 512
img = cv.resize(img, (Nc, Nf))

# Img to gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Img to numpy float f(x,y)
img_gray_float = np.float64(img_gray)

# Spectrum with fourer transform
Fuv = np.fft.fft2(img_gray_float)   # 2d fourier
Fuv = np.fft.fftshift(Fuv)          # low freq in center

# Magnitude
Fuv_abs = np.abs(Fuv)

# Spectrum in log scale
Fuv_log = 20*np.log10(Fuv_abs)

cv.imshow('img', img_gray)
cv.imshow('img_fourier', np.uint8(255*Fuv_log/np.max(Fuv_log)))

# ------------ High pass filter
F1 = np.arange(-Nf/2+1, Nf/2+1, 1)  # x
F2 = np.arange(-Nc/2+1, Nc/2+1, 1)  # y
[X, Y] = np.meshgrid(F1, F2)        # x + y
D = np.sqrt(X**2+Y**2)
D = D/np.max(D)

# Cut radius
Do = 0.24
# Ideal 2D filter
Huv = np.zeros((Nf, Nc))
for i in range(Nf):
    for j in range(Nc):
        if D[i, j] < Do:
            Huv[i, j] = 1
# Convert to pass high
Huv = 1-Huv
# ---------------------

# Show high pass
cv.imshow('High pass', np.uint8(255*Huv))

# Frecuency filtering
Guv = Huv * Fuv
# Compute magnitude
Guv_abs = np.abs(Guv)
Guv_abs = np.uint8(255*Guv_abs/np.max(Guv_abs))
cv.imshow('Frecuency spectrum G', Guv_abs)

# ----------- Inverse fourier transform
gxy = np.fft.ifft2(Guv)
gxy = np.abs(gxy)
gxy = np.uint8(gxy)
cv.imshow('Filtered image', gxy)

cv.waitKey(0)
