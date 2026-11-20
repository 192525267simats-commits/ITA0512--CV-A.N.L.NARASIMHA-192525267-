import cv2
import numpy as np

img = cv2.imread("input.jpg")

kernel = np.ones((9, 9), np.uint8)

black_hat = cv2.morphologyEx(
    img,
    cv2.MORPH_BLACKHAT,
    kernel
)

cv2.imshow("Original", img)
cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()