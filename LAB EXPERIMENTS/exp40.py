import cv2

img = cv2.imread("input.jpg")

# Coordinates of object
x1, y1 = 50, 50
x2, y2 = 250, 250

# Draw rectangle
cv2.rectangle(
    img,
    (x1, y1),
    (x2, y2),
    (0, 255, 0),
    2
)

# Extract object
object_img = img[
    y1:y2,
    x1:x2
]

# Save extracted object
cv2.imwrite(
    "extracted_object.jpg",
    object_img
)

cv2.imshow(
    "Selected Object",
    img
)

cv2.imshow(
    "Extracted Object",
    object_img
)

cv2.waitKey(0)
cv2.destroyAllWindows()