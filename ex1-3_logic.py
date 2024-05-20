import cv2
import matplotlib.pyplot as plt

image1 = cv2.imread("images/Lenna.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/mask.jpg", cv2.IMREAD_GRAYSCALE)

image1 = cv2.resize(image1, dsize=(500,500), interpolation=cv2.INTER_CUBIC)
image2 = cv2.resize(image2, dsize=(500,500), interpolation=cv2.INTER_CUBIC)

output1 = cv2.bitwise_and(image1, image2)

# view
img_list = [image1, image2, output1]
title_list = ['image1', 'image2', 'OpenCV']

for i in range(len(img_list)):
    plt.subplot(2, 2, i+1)
    plt.imshow(img_list[i], cmap='gray')
    plt.title(title_list[i])
    plt.axis('off')
plt.show()