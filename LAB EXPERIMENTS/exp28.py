import cv2
import numpy as np

img = cv2.imread(
    "input.jpg",
    cv2.IMREAD_GRAYSCALE
)

kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
], dtype=np.float32)

boundary = cv2.filter2D(
    img,
    cv2.CV_32F,
    kernel
)

boundary = cv2.convertScaleAbs(
    boundary
)

cv2.imshow(
    "Boundary",
    boundary
)

cv2.waitKey(0)
cv2.destroyAllWindows()