import cv2
import numpy as np
import math
pi = math.pi
#Şeklin orta noktasından bütün
#kontürlere olan uzaklığın hesaplanması
# ardından sıralanarak belli uzaklıklar arası
# düşük bir hata payı elde etmekti.
img = cv2.imread("images/shapes.png", 0)
img = cv2.resize(img, (551,551))
ret, thr = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thr, cv2.MORPH_CLOSE,kernel)
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
images = []
font = cv2.FONT_HERSHEY_COMPLEX
for i in range(len(contours)):
    for j in range(len(contours[i])):
        cnt = contours[i]
        perimeter = cv2.arcLength(contours[i], True)
        M = cv2.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        x = (contours[i][j][0])[0]
        y = (contours[i][j][0])[1]
        # print(x,y)
        metric= float(format(((math.sqrt(pow((cx-x),2)+ pow((cy-y),2))))/math.sqrt(perimeter), '.4f'))
        images.append(metric)
        images.sort(reverse = True)
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        rect_area = w * h
        extent = float(area) / rect_area
    print(images)

cv2.waitKey(0)
cv2.destroyAllWindows()