import cv2

# Read image
img = cv2.imread("image.jpg")

# Create copy
watermark = img.copy()

# Add watermark text
cv2.putText(watermark, "OpenCV Lab", (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255,255,255), 2)

# Blend images
result = cv2.addWeighted(watermark, 0.3, img, 0.7, 0)

cv2.imshow("Original", img)
cv2.imshow("Watermarked Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()