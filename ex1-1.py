import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.util import invert

image = cv2.imread("images/tsla.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 직접 계산
output1 = 255 - image

# numpy 라이브러리
output2 = np.invert(image)

# OpenCV 라이브러리
output3 = cv2.bitwise_not(image)

# scikit-image 라이브러리
output4 = invert(image)

# view
img_list = [image, output1, output2, output3, output4]
title_list = ['Original', 'Calculate', 'Numpy', 'OpenCV', 'Scikit-image']

for i in range(len(img_list)):
    plt.subplot(2, 3, i+1)
    plt.imshow(img_list[i], cmap='gray')
    plt.title(title_list[i])
    plt.axis('off')
plt.show()