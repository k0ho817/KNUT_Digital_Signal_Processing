import cv2
import numpy as np
# def on_threshold(pos):
#     _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
#     print(dst)
#     TP_dst = dst>0
#     TP_dst_sum = TP_dst.sum(axis=1)
#     cv2.line(src, (0, 10), (100, 200), (255, 0, 0), 2)
#     cv2.imshow('dst', dst)
#
# src = cv2.imread('images/tire.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('src', src)
# cv2.namedWindow('dst')
# cv2.createTrackbar('Threshold', 'dst', 0, 255, on_threshold)
# cv2.setTrackbarPos('Threshold', 'dst', 255)
#
# cv2.waitKey(0)
def find_steep_changes(lst, threshold):
    steep_changes = []
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i-1]) > threshold:
            steep_changes.append(i)
    return steep_changes

origin_image = cv2.imread("images/tire.png", cv2.IMREAD_COLOR)
image = cv2.imread("images/tire.png", cv2.IMREAD_GRAYSCALE)
h,w = image.shape
ret, dst = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
TF_img = dst > 0
TF_img_sum = TF_img.sum(axis=1)
tire_y = find_steep_changes(TF_img_sum,58)
tire_parts1 = cv2.line(image_dst, (0, tire_y[0]), (w, tire_y[0]), (255, 255, 255), 5)
tire_parts2 = cv2.line(tire_parts1, (0, tire_y[-1]), (w, tire_y[-1]), (255, 255, 255), 5)

cv2.imshow("Original Image", dst)
cv2.imshow('tire_parts', tire_parts2)
cv2.waitKey(0)