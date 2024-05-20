import cv2

img = cv2.imread("images/Lenna.jpg")
# img2 = cv2.resize(img, dsize=(0, 0), fx=2, fy=2)  # 이미지 확대
img2 = cv2.resize(img, dsize=(400, 400))

filter_img = cv2.GaussianBlur(img2, (7, 7), 1)
filter_img2 = cv2.GaussianBlur(img2, (0, 0), 3)

cv2.imshow("Lenna", img2)
cv2.imshow("filter_img", filter_img)
cv2.imshow("filter_img2", filter_img2)

cv2.waitKey()
cv2.destroyAllWindows()