'''import numpy as np
import argparse
import cv2
from skimage.exposure import rescale_intensity

def convolve(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * kernel).sum()
			output[y - pad, x - pad] = k
	output = np.absolute(output)
	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")

	return output

ramonEdger = np.array((
	[-1, -5, -2, 1, 1],
	[-5, -2, -4, 2, 1],
	[-4, -4, 0, 4, 4],
    [-1, -2, 4, 2, 5],
    [-1, -1, 2, 5, 1]), dtype="int")

image = cv2.imread("images/amro.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

convolveOutput = convolve(gray, ramonEdger)
cv2.imshow("original", gray)
convolveOutput[convolveOutput < 255] = 0
cv2.imshow("CONVOLUCIONADO",convolveOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/amro.jpg',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv2.imwrite("AAA.jpg", edges)
plt.show()