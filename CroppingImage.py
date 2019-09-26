import cv2
import numpy
#cropping image according to contours
img = cv2.imread("images/shapes.png", 0)
img = cv2.resize(img, (500, 500))
# cv2.imshow("original", img)
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
images = []
idx = 0
for i in range(len(contours)):
    cnt = contours[i]
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    x,y,w,h = cv2.boundingRect(cnt)
    print(w*h)

    if(w*h < 25000):
        images.append(img[y-30:y+h+30,x-30:x+w+30])
        cv2.imshow("images"+str(idx),images[idx])
        contours1, hierarchy1 = cv2.findContours(images[idx], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        idx += 1

cv2.waitKey()
cv2.destroyAllWindows()