import cv2

img = cv2.imread("input.jpg")
template = cv2.imread("watch_template.jpg")

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

temp_gray = cv2.cvtColor(
    template,
    cv2.COLOR_BGR2GRAY
)

result = cv2.matchTemplate(
    gray,
    temp_gray,
    cv2.TM_CCOEFF_NORMED
)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

threshold = 0.70

if max_val >= threshold:

    h, w = temp_gray.shape

    cv2.rectangle(
        img,
        max_loc,
        (max_loc[0] + w, max_loc[1] + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        "WATCH",
        max_loc,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

cv2.imshow("Watch Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()