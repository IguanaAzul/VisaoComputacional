import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

nomeImagem = "images/NoisyBear.png"
img = cv.imread(nomeImagem, 0)
cv.imshow("queijo1", img)
img = cv.GaussianBlur(img,(5,5),0)

hist,bins = np.histogram(img.flatten(),256,[0,256]) 
r = 4
cdf = hist.cumsum() ** r
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img = cdf[img]

cv.imshow("queijo2", img)

hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv.waitKey()