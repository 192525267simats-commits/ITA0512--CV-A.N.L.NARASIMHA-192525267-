import cv2

img = cv2.imread("input.jpg")

cv2.putText(
    img,
    "MY WATERMARK",
    (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.imwrite(
    "watermarked.jpg",
    img
)

cv2.imshow(
    "Watermarked Image",
    img
)

cv2.waitKey(0)
cv2.destroyAllWindows()