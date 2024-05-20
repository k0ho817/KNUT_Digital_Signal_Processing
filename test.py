import numpy as np
import cv2

img = cv2.imread('images/car1.jpg')

pos_x = 0
pos_y = 0
def pt2_x_handler(pos):
    image = np.zeros((512,512,3), np.uint8)
    image = cv2.line(image, (0, 0), (pos, 0), (255, 0, 0), 5)
    cv2.imshow("image", image)

cv2.namedWindow('image')
cv2.createTrackbar('pt2 X','image', 0, 400, pt2_x_handler)
cv2.setTrackbarPos('pt2_X', 'image', 255)
cv2.waitKey(0)

x = [1, 2, 3, 4, 5]

np_x = np.array(x, float) # ndarray

print(np_x)

x = [1, 2, 3, 4, "5"]
print(x)
print(type(x[4]))

np_x = np.array(x, float) # ndarray
print(np_x)
print(type(np_x[4]))
print(np_x.dtype)
print(np_x.shape) # vector/matrix/tensor 등의 크기, 형태 등에 대한 정보를 1차원 vector)

x = [[1,2,3,4,5], [2,5,3,4,4], [2,4,5,6,4]]
x = np.array(x, int)
print(x.shape) # (3 X 5 크기의 행렬이다.)