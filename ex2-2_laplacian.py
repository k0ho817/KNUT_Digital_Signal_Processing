import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../../week5/DIP_ex2/images/Lenna.jpg', cv2.IMREAD_GRAYSCALE)

mask1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
mask2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
mask3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

laplacian1 = cv2.filter2D(img, -1, mask1)
laplacian2 = cv2.filter2D(img, -1, mask2)
laplacian3 = cv2.filter2D(img, -1, mask3)
laplacian4 = cv2.Laplacian(img, -1)

plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Input image")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(laplacian1, cmap='gray')
plt.title("mask1")

plt.subplot(2, 3, 3)
plt.imshow(laplacian2, cmap='gray')
plt.title("mask2")

plt.subplot(2, 3, 4)
plt.imshow(laplacian3, cmap='gray')
plt.title("mask3")

plt.subplot(2, 3, 5)
plt.imshow(laplacian4, cmap='gray')
plt.title("opencv laplacian")

plt.show()