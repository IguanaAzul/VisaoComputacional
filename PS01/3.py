import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread("images/lagolaogai.png", 0)
img2 = cv.imread("images/tubarao.png", 0)

ft1 = np.fft.fft2(img1)
modulo1 = np.absolute(ft1)
angulo1 = np.angle(ft1)

ft2 = np.fft.fft2(img2)
modulo2 = np.absolute(ft2)
angulo2 = np.angle(ft2)

angulo1 = angulo2 = (angulo1+angulo2)/2

img3 = modulo1*(np.sin(angulo2)*1j + np.cos(angulo2))
img4 = modulo2*(np.sin(angulo1)*1j + np.cos(angulo1))

img3 = np.ndarray.astype(np.absolute(np.fft.ifft2(img3)), np.uint8)
img4 = np.ndarray.astype(np.absolute(np.fft.ifft2(img4)), np.uint8)

cv.imshow("alo", img3)
cv.imshow("alo2", img4)
cv.waitKey()