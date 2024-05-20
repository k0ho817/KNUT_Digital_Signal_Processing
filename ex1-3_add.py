import cv2
import matplotlib.pyplot as plt


image1 = cv2.imread("images/Lenna.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/cameraman.jpg", cv2.IMREAD_GRAYSCALE)

image1 = cv2.resize(image1, dsize=(500,500), interpolation=cv2.INTER_CUBIC)
image2 = cv2.resize(image2, dsize=(500,500), interpolation=cv2.INTER_CUBIC)

output1 = cv2.add(image1, image2, dtype=cv2.CV_8U) # 두 영상의 같은 위치에 있는 픽셀들의 값을 더하여 결과 값으로 출력
output2 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0.0) # 가중치를 곱하여 두 영상간 합을 생성

img_list = [image1, image2, output1, output2]
title_list = ['image1', 'image2', 'OpenCV', 'OpenCV_weighted']

for i in range(len(img_list)):
    plt.subplot(2, 2, i+1)
    plt.imshow(img_list[i], cmap='gray')
    plt.title(title_list[i])
    plt.axis('off')
plt.show()