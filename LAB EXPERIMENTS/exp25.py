import cv2
import numpy as np

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY
)

gx = cv2.Sobel(
    gray, cv2.CV_32F, 1, 0, ksize=3
)

gy = cv2.Sobel(
    gray, cv2.CV_32F, 0, 1, ksize=3
)

gradient = cv2.magnitude(gx, gy)

gradient = cv2.normalize(
    gradient, None, 0, 255,
    cv2.NORM_MINMAX
)

mask = gradient.astype(np.uint8)

mask = cv2.cvtColor(
    mask, cv2.COLOR_GRAY2BGR
)

sharp = cv2.add(img, mask)

cv2.imshow("Original", img)
cv2.imshow("Gradient Masking", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()