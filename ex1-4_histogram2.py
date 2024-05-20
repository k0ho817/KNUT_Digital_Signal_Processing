import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
print("original data: ", img)
img_hist = cv2.calcHist([img], [0], None, [256], [0,256])

x = np.arange(256)
y = np.squeeze(img_hist, axis=1)
print("histogram: ", img_hist)
print(sum(img_hist))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Input image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Histogram")
plt.show()

