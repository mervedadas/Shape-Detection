import cv2
import numpy as np
import math
import copy

img = cv2.imread("images/thr.jpg", 0)
img = cv2.resize(img, (500, 500))
cv2.imshow("original", img)
clone_img = copy.copy(img)
# cv2.imshow("copy",clone_img)
img=cv2.blur(img,(5,5))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17,17))
kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (17,17))
erode = cv2.erode(img,kernel,iterations = 1)
# cv2.imshow("erosion",img)
print(clone_img.dtype)
img2_fg = cv2.bitwise_and(erode,erode,mask = clone_img)
img2_fg= cv2.blur(img2_fg,(5,5))
# cv2.imshow("hahah",img2_fg)
contours, hierarchy = cv2.findContours(img2_fg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


edges=[]
blackhat=[]
blackhat1=[]
final=[]
images = []
font = cv2.FONT_HERSHEY_COMPLEX

for i in range(len(contours)):

    cnt = contours[i]
    M = cv2.moments(cnt)
    if(M['m00']!=0):
        x = int(M['m10'] / M['m00'])
        y = (M['m01'] / M['m00'])
    # print (cx,cy)
    x,y,w,h = cv2.boundingRect(cnt)
    if(w*h >250):
        images.append(img2_fg[y-30:y+h+30,x-30:x+w+30])
        # print(x,y)

print(len(images))

for i in range(len(images)):
    if(i==4):
        break
    cnt = images[i]
    M = cv2.moments(cnt)
    if (M['m00'] != 0):
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    # cv2.imshow("aa" + str(i), aa[i])
    edges.append(cv2.Canny(images[i], 100, 200))
    cv2.imshow("edges" + str(i), edges[i])
    blackhat.append(cv2.morphologyEx(edges[i], cv2.MORPH_BLACKHAT, kernel))
    blackhat1.append (cv2.morphologyEx(edges[i], cv2.MORPH_BLACKHAT, kernel1))
    final.append (cv2.bitwise_not(blackhat[i], blackhat[i], mask=blackhat1[i]))
    kernel45 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    final[i] = ( cv2.filter2D(final[i], -1, kernel45))
    final[i] = cv2.blur(final[i], (9,9))
    final[i] = cv2.morphologyEx(final[i], cv2.MORPH_OPEN, kernel1)
    cv2.imshow("Final" + str(i), final[i])
    contours_crop, hierarchy_crop = cv2.findContours(final[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours_crop))
    cnt =contours_crop[0]
    M = cv2.moments(cnt)
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])

    # if (len(contours_crop) == 6):
    #      cv2.putText(clone_img, "hexagon", (x, y), font, 1, (0))
    # elif (len(contours_crop) == 4):
    #      cv2.putText(clone_img, "rectangle", (x, y), font, 1, (0))
    # elif (len(contours_crop) == 5):
    #     cv2.putText(clone_img, "pentagon", (x, y), font, 1, (0))
    # elif (len(contours_crop) == 3):
    #     cv2.putText(clone_img, "triangle", (x, y), font, 1, (0))
    # elif (len(contours_crop) >= 8 ):
    #     cv2.putText(clone_img, "ellipse", (x, y), font, 1, (0))

cv2.waitKey()
cv2.destroyAllWindows()