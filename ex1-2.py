import cv2

def on_threshold(pos):
    _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

# imread("image address", cv2.IIMREAD_GRAYSCALE <- 회색조 영상)
src = cv2.imread('images/tsla.jpg', cv2.IMREAD_GRAYSCALE)


cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos('Threshold', 'dst', 255)

cv2.waitKey(0)