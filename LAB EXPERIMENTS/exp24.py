import cv2
import numpy as np

img = cv2.imread("input.jpg")

img_float = img.astype(np.float32)

blur = cv2.GaussianBlur(
    img_float, (5, 5), 0
)

A = 1.5

high_boost = A * img_float - blur

high_boost = np.clip(
    high_boost, 0, 255
).astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("High Boost", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()