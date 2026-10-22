import cv2
import numpy as np

# Read grayscale image
img = cv2.imread("image.jpg", 0)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Dilated Image", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()