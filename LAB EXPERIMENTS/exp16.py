import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel along X-axis
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel along Y-axis
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine X and Y
sobel = cv2.magnitude(sobelx, sobely)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel Edge Detection", sobel.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()