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
rows, cols = img.shape
crow = int(rows/2)
ccol = int(cols/2)

lowpass = np.zeros((rows,cols,2), np.float32)
cv2.circle(lowpass, (crow, ccol), 40, (1,1), -1) # lowpass 필터의 크기 설정 radius

highpass = np.ones((rows,cols,2), np.float32)
cv2.circle(highpass, (crow, ccol), 230, (0,0), -1) # highpass 필터의 크기 설정 radius

gaussian_f = np.zeros((rows,cols,2), np.float32)
sigma = 2 * 30 * 30
for i in range(rows):
    for j in range(cols):
        x2 = (j - ccol) * (j-ccol)
        y2 = (i - crow) * (i-crow)
        w = np.exp(-(x2+y2)/sigma)
        gaussian_f[i,j] = (w,w)

dft=cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

F_dft_shift = cv2.multiply(dft_shift, lowpass) # lowpass, highpass, gaussian_f 변경
i_F_dft_shift = np.fft.fftshift(F_dft_shift)

img_back = cv2.idft(i_F_dft_shift)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,0])

displayDFT("dft",F_dft_shift)

inverse_DFT = cv2.normalize(np.abs(img_back),None,0,1,cv2.NORM_MINMAX)
cv2.imshow("Original image", img)
cv2.imshow("inverse_DFT", inverse_DFT)

cv2.waitKey(0)