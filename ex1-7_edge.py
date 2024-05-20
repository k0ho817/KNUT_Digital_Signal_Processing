import cv2

img = cv2.imread('images/Lenna.jpg')
img = cv2.resize(img, dsize=(720, 720))
# canny를 적용하기 전에 흑백전환을 하지 않아도 된다.
output = cv2.Canny(img, 60, 200) # 처리할 이미지 사진 / min Threshold / max Threshold
# output = cv2.Laplacian(img, -1)

cv2.imshow('before', img)
cv2.imshow('After', output)
cv2.waitKey(0)
cv2.destroyAllWindows()