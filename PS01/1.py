import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

nomeImagem = "images/king.png"
img = cv.imread(nomeImagem)

def histogram(img):
   plt.clf()
   color = ('b', 'g', 'r')
   for i,col in enumerate(color):
      histr = cv.calcHist([img],[i],None,[256],[0,256])
      plt.plot(histr,color = col)
      plt.xlim([0,256])
   plt.show()

def mousePosition(event,x,y,flags,param):
   if(event == cv.EVENT_MOUSEMOVE):
      temp=img.copy()
      color = img[y,x]
      intensity = np.average(img[y,x])
      mean = np.average(img[y-5:y+6, x-5:x+6])
      std = np.std(img[y-5:y+6, x-5:x+6])
      print("x =", x, "y =", y, "color  =", color, "intensity = ", intensity, "mean intensity =", mean, "standard deviation =", std)
      pt1 = (x-5, y-5)
      pt2 = (x+5, y+5)
      cv.rectangle(temp, pt1, pt2, (255, 0, 0), 1)
      cv.imshow("queijo", temp)
   if(event == cv.EVENT_LBUTTONDBLCLK):
      histogram(img[y-5:y+6, x-5:x+6])
   if(event == cv.EVENT_RBUTTONDOWN):
      histogram(img)

cv.imshow("queijo", img)
cv.setMouseCallback("queijo",mousePosition)
histogram(img)
cv.waitKey()
