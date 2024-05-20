import cv2
import sys
src = cv2.imread('./images/morph_dot.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) # 가로 5, 세로 3
dst1 = cv2.erode(src, se)


cv2.imshow('src', src)
cv2.imshow('dst1', dst1)

cv2.waitKey()
cv2.destroyAllWindows()