import cv2
import numpy as np
import math
pi = math.pi
#makalelerde sunulan iki farklı
# metric çözüm önerisinin uygulamaya konması.
# Metric değerleri birbirine çok yakın
# çıktığı için başarı oranı düşük.
img = cv2.imread("images/shapes.png", 0)
img = cv2.resize(img, (600, 600))
# cv2.imshow("org",img)
ret, thr = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("threshold", thr)
kernel = np.ones((15,15), np.uint8)
contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX
for i in range(0, 5):
        area = cv2.contourArea(contours[i])
        cv2.drawContours(img,contours[i], 0, (0,255,0), 2, 100)
        perimeter = cv2.arcLength(contours[i], True)
        metric1 = float(format(math.sqrt(((4*pi*area)/(pow(perimeter, 2)))), '.5f'))
        metric2 = float(area/pow(perimeter,2))
        cnt = contours[i]
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        if metric1 < 0:
            cv2.putText(img, "Rectangle", (cx, cy), font, 1, (0))
        elif metric1 < 0.45:
            cv2.putText(img, "Triangle", (cx, cy), font, 1, (0))
        elif metric1 < 0.15:
            cv2.putText(img, "Circle", (cx, cy), font, 1, (0))
        print(i+1, " shape metric" , metric1)
cv2.imshow("final", img)
cv2.waitKey(0)
cv2.destroyAllWindows()