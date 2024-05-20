import cv2

cap = cv2.VideoCapture("./images/reporter_chromakey.mp4")
background_img = cv2.imread("./images/sejong.jpg")
# 크로마키 색상 추출하여 날려버린다.

while cap.isOpened():
    success, frame = cap.read()
    h, w = frame.shape[:2]
    frame = cv2.resize(frame, dsize=(int(w/2), int(h/2)), interpolation=cv2.INTER_CUBIC)
    background_img = cv2.resize(background_img, dsize=(int(w/2), int(h/2)), interpolation=cv2.INTER_CUBIC)
    # print(background_img.shape)
    if success:
        converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        green_screen = cv2.inRange(converted, (60 - 20, 120, 0), (60 + 20, 255, 255))

        inverted = cv2.bitwise_not(green_screen)
        dst = cv2.bitwise_and(frame, frame, mask=inverted)
        dst1 = cv2.bitwise_or(dst, background_img, mask=green_screen)
        dst1 = cv2.bitwise_or(dst, dst1)

        cv2.imshow("chroma_img", frame)
        cv2.imshow("green", green_screen)
        cv2.imshow("dst", dst)
        cv2.imshow("dst1", dst1)


        key = cv2.waitKey(10) & 0xFF

        if (key == 27):
            break
    else:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()