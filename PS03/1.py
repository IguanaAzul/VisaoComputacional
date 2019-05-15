import numpy as np
import cv2


def components(labels):
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    labeled_img[label_hue==0] = 0
    return labeled_img

img = cv2.imread("images/bricks.jpg",0)
cv2.imshow('image', img)
threshold = 140
img[img < threshold] = 0
img[img >= threshold] = 255
cv2.imshow('thresholdedImage', img)

ret, labels = cv2.connectedComponents(img, connectivity = 8)
print(ret), print('tipo: '), print(type(ret))
show = components(labels)
f = open('txt.txt', 'w+')
for x in labels:
    for y in labels:
        f.write(str(labels[x,y]))
        f.write(' ')
    f.write('\n')
f.close()
cv2.imshow('labeled_8way', show)

def mousePosition(event,x,y,flags,param):
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        print("Area = " + img.sum(labels[x, y]))

cv2.setMouseCallback('labeled_8way', mousePosition)

cv2.waitKey()
cv2.destroyAllWindows()