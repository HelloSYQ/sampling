#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import cv2


# cut a rectangle image within x, y, x, y are np.array
def img_cutter(img,x,y):
	img_cut = img(x,y)
	return img_cut

def img_center(img,x,y):
	img_center_x = np.sum(np.dot(img.T,x))/np.sum(img)
	img_center_y = np.sum(np.dot(img,y))/np.sum(img)
	return [img_center_x,img_center_y]

#img = cv2.imread('testsun.jpeg',cv2.IMREAD_GRAYSCALE)
#img_cr_x = np.arange(img.shape[0])
#img_cr_y = np.arange(img.shape[1])
#img_center = img_center(img,img_cr_x,img_cr_y)

L = 40
X = np.arange(-L, L+1, 1.0)
Y = np.arange(-2*L, 2*L+1, 1.0)
X1, Y1 = np.meshgrid(X, Y)
R = (X1**2 + Y1**2)
sigma = 3
img_Z = np.exp(-R/(2*sigma**2))

img_cr_x = np.arange(img_Z.shape[0])
img_cr_y = np.arange(img_Z.shape[1])
img_center = img_center(img_Z,img_cr_x,img_cr_y)
center_z = np.round(img_center)
center_z = center_z.astype(np.int)
print(center_z)
img_Z[center_z[0]][center_z[1]] = 0

fig = plt.imshow(img_Z)
plt.savefig('center_find.png',dpi = 300)