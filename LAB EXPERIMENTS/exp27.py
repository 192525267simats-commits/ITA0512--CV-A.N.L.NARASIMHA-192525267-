import cv2

img = cv2.imread("input.jpg")

# Crop the region
crop = img[50:200, 50:200].copy()

# Paste the cropped region
h, w = crop.shape[:2]

img[250:250+h, 250:250+w] = crop

cv2.imshow(
    "Copy and Paste",
    img
)

cv2.imshow(
    "Cropped Image",
    crop
)

cv2.waitKey(0)
cv2.destroyAllWindows()