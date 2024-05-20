import sys
import cv2
# import numpy as np

#흑백으로 만듦
src = cv2.imread('images/mountain.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('image load failed!')
    sys.exit()

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()