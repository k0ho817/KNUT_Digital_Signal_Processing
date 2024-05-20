import cv2


cap = cv2.VideoCapture("./images/video_car.mp4")
# cap = cv2.VideoCapture(0) # 카메라 인식

while cap.isOpened():
    success, frame = cap.read()
    h, w = frame.shape[:2]
    frame = cv2.resize(frame, dsize=(int(w/2), int(h/2)), interpolation=cv2.INTER_CUBIC)
    if success:
        imgThresholded = cv2.inRange(frame, (100,50,0), (255,255,100))
        cv2.imshow("imgThresholded", imgThresholded)
        cv2.imshow("camera", frame)
        key = cv2.waitKey(10) & 0xFF
        print("1")
        if (key == 27):
            break
    else:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()