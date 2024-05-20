import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import invert

image = cv2.imread("images/Einstein.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gamma = 0.6 #값이 커질수록 어두워진다.

image = image.astype(np.float32)

output1 = np.uint8(((image / 255) ** gamma) * 255)

# view
img_list = [image, output1]
title_list = ['Original', 'Gamma']

for i in range(len(img_list)):
    plt.subplot(1, 2, i+1)
    plt.imshow(img_list[i], cmap='gray')
    plt.title(title_list[i])
    plt.axis('off')
plt.show()