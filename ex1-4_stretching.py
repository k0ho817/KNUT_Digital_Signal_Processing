import sys
import cv2
import numpy as np

src = cv2.imread('images/mountain.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

# gmin = np.min(src)
# gmax = np.max(src)
# dst = np.clip((src - gmin) * 255. / (gmax - gmin), 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()