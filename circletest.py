#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('cic.png',cv2.IMREAD_GRAYSCALE)



plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.xticks([])
plt.yticks([])
#hough transform
circles1 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=200,maxRadius=300)
circles = circles1[0,:,:]#提取为二维
print(circles)

circles = np.uint16(np.around(circles))#四舍五入，取整
for i in circles[:]: 
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)#画圆
    cv2.circle(img,(i[0],i[1]),2,(255,255,0),10)#画圆心

plt.subplot(122)
plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.savefig('cictest.png',dpi=300)