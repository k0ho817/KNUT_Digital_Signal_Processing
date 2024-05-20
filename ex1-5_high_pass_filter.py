import cv2
import numpy as np

img = cv2.imread('images/Lenna.jpg')

#3x3 평균 필터 커널 생성
#laplacian filter
# kernel = np.array([[0, 1, 0],
#                    [1, 9, 1],
#                    [0, 1, 0]])
#laplacian 대각항 포함 1
# kernel = np.array([[1, 1, 1],
#                    [1, 9, 1],
#                    [1, 1, 1]])
#laplacian 대각항 포함 2
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])


# 필터 적용             ---③
output = cv2.filter2D(img, -1, kernel)

# 결과 출력
cv2.imshow('origin', img)
cv2.imshow('HPF', output)
cv2.waitKey()
cv2.destroyAllWindows()