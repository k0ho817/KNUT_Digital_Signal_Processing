import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(img): #use counting sort
    h,w = img.shape[:2]
    cnt = np.array([0 for i in range(256)])
    for i in range(h):
        for j in range(w):
            cnt[int(img[i][j])] += 1
    return cnt

def CDF(hist):
    cnt = np.array([0 for i in range(256)])
    for i, p in enumerate(hist):
        if i > 0:
            cnt[i] = (cnt[i-1] + hist[i])
        else:
            cnt[i] = hist[i]
    return cnt


img = cv2.imread('../../week5/DIP_ex2/images/mountain.jpg', cv2.IMREAD_GRAYSCALE)
print("original data: ", img)
img_hist = histogram(img)
h,w = img.shape[:2]
cdf = CDF(img_hist) / (h*w)

x = np.arange(256)
y = img_hist
print("histogram: ", img_hist)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Input image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.bar(x, y)
plt.title("Histogram")

plt.subplot(1, 3, 3)
plt.bar(x, cdf)
plt.title("Cumulative Distribution Function")
plt.show()