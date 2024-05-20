import cv2
import numpy as np

img = cv2.imread('images/Lenna.jpg')
'''
#3x3 평균 필터 커널 생성
kernel = np.array([[0.11, 0.11, 0.11],
                   [0.11, 0.11, 0.11],
                   [0.11, 0.11, 0.11]])
'''
# 5x5 평균 필터 커널 생성  ---②
kernel = np.ones((7,7))/3**2
# 필터 적용             ---③
blured = cv2.filter2D(img, -1, kernel)

# 결과 출력
cv2.imshow('origin', img)
cv2.imshow('avrg blur', blured)
cv2.waitKey()
cv2.destroyAllWindows()