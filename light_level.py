import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('einstein.jpg')

hist=cv2.calcHist([img],[1],None,[255],[0,255])
plt.subplot(2,1,1)
plt.imshow(img,'gray')
plt.subplot(2,1,2)
plt.plot(hist)
plt.show()