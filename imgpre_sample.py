#!/usr/bin/python3

# objective: 1 read 2 downsampled image
#            2 reconstruct them with 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from scipy.integrate import quad
from scipy.linalg import inv
from scipy.linalg import det

# calculate shape (function) matrix


test_img = cv2.imread('massimo.jpg')
test_img1 = test_img[0:505,0:505,0]

# Add Gaussian distribution
L = 252
X = np.arange(-L, L+1, 1.0)
Y = np.arange(-L, L+1, 1.0)
X1, Y1 = np.meshgrid(X, Y)
R = (X1**2 + Y1**2)
sigma = 100
Gaussian_F = np.exp(-R/(2*sigma**2))

test_img_F = np.multiply(test_img1,Gaussian_F)

# image downsample by sample pixels
img_sampix = np.zeros((101,101))

# image downsample by pixel average
img_samavg = np.zeros((101,101))

# inverse Gaussian filter
inv_gauss = np.zeros((101,101))

for i in range(0,101):
	for j in range(0,101):
		img_sampix[i,j] = test_img_F[5*i+2,5*j+2]
		img_samavg[i,j] = np.mean(test_img_F[5*i:5*(i+1),5*j:5*(j+1)])
		inv_gauss[i,j] = Gaussian_F[5*i+2,5*j+2]
		if (i == 0 and j ==0):
			print(img_samavg[i,j])


np.save('sampix.npy',img_sampix)
np.save('samavg.npy',img_samavg)
np.save('inv_gauss.npy',inv_gauss)

cv2.imwrite('nosamimg.png',test_img1)
cv2.imwrite('sampix.png',img_sampix)
cv2.imwrite('samavg.png',img_samavg)




