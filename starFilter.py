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

# 레나 이미지 로드
img = cv2.imread("../../week6/ex3/images/Lenna.jpg", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape
crow = int(rows/2)
ccol = int(cols/2)

# 필터 이미지 로드
filter_img = cv2.imread("./images/starFilter.jpg", cv2.IMREAD_GRAYSCALE)
filter_img = cv2.resize(filter_img, (cols, rows))

# 필터 이미지의 DFT 계산
filter_dft = cv2.dft(np.float32(filter_img), flags=cv2.DFT_COMPLEX_OUTPUT)
filter_dft_shift = np.fft.fftshift(filter_dft)

# 입력 이미지의 DFT 계산
dft=cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# 필터 적용
F_dft_shift = cv2.multiply(dft_shift, filter_dft_shift)

# 역 DFT 적용
i_F_dft_shift = np.fft.fftshift(F_dft_shift)
img_back = cv2.idft(i_F_dft_shift)
img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,0])

# DFT 결과 및 역 DFT 결과 표시
displayDFT("dft", F_dft_shift)
inverse_DFT = cv2.normalize(np.abs(img_back), None, 0, 1, cv2.NORM_MINMAX)
cv2.imshow("Original image", img)
cv2.imshow("inverse_DFT", inverse_DFT)
cv2.waitKey(0)
