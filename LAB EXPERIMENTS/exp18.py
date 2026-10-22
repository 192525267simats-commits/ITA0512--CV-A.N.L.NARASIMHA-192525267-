import cv2

# Read image
img = cv2.imread("image.jpg")

# Crop ROI
roi = img[50:200, 50:200]

# Paste ROI to another location
img[220:370, 220:370] = roi

cv2.imshow("Modified Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()