import cv2
import numpy as np

def displayDFT(name, src):
    src1 = src[:,:,0]
    src2 = src[:,:,1]
    mag_image = cv2.magnitude(src1,src2)
    mag_image += 1
    spectrum = np.log(np.abs(mag_image))
    dft=cv2.normalize(spectrum,None,0,1,cv2.NORM_MINMAX)
    cv2.imshow(name,dft)


img = cv2.imread("../../week6/ex3/images/Lenna.jpg", cv2.IMREAD_GRAYSCALE)

dft = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
dft = np.fft.fftshift(dft)
# 필터링 연산이 들어가게 된다.
dft = np.fft.fftshift(dft)
img_back = cv2.idft(dft)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,0])

displayDFT("dft",dft)

inverse_DFT = cv2.normalize(np.abs(img_back),None,0,1,cv2.NORM_MINMAX)
cv2.imshow("Original image", img)
cv2.imshow("inverse_DFT", inverse_DFT)

cv2.waitKey(0)