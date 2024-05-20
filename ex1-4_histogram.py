import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(img):#use counting sort
    h,w = img.shape[:2]
    cnt = np.array([0 for i in range(256)]) #유용함
    for i in range(h):
        for j in range(w):
            cnt[int(img[i][j])] += 1
    return cnt

img = cv2.imread('images/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
print("original data: ", img)
img_hist = histogram(img)
x = np.arange(256)
y = img_hist
print("histogram: ", img_hist)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Input image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Histogram")
plt.show()

