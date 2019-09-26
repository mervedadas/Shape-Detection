import cv2
import numpy as np

img = cv2.imread("images/shapes oki.jpg", 0)
img = cv2.resize(img, (800, 600))
# cv2.imshow("org", img)
ret, thr = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh', thr)
cv2.imwrite("thr.jpg", thr)
kernel = np.ones((7, 7), np.uint8)
opening = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel)  #erode + dilation
cv2.imshow("opening", opening)
contours, ret = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.03*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, -1, 2, 10)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, 1, (0))
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x+50, y+50), font, 1, (0))
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), font, 1, (0))
    elif len(approx) == 8:
        cv2.putText(img, "octagonal", (x, y), font, 1, (0))
    elif 8 < len(approx) < 12:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "Circle", (x, y), font, 1, (0))

cv2.imshow("shapes", img)
cv2.waitKey()
cv2.destroyAllWindows()