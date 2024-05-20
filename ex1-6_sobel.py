import cv2

img = cv2.imread('images/Lenna.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, dsize=(720, 720))

output = cv2.Sobel(img, cv2.CV_8U, 1,0,3)

cv2.imshow('before', img)
cv2.imshow('After', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
