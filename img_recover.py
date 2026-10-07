#!/usr/bin/python3

# objective: 1 read 2 downsampled image
#            2 reconstruct them with 

import matplotlib.pyplot as plt
import cv2
import numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from scipy.integrate import quad
from scipy.linalg import inv
from scipy.linalg import det


# calculate shape (function) matrix
'''
def CalcMat(L,sgap):
	MatR = np.zeros([2*L+1,2*L+1])
	for i in range(-L,L+1):
		for j in range(-L,L+1):
			def functionx(x):
				return np.sinc((i-x/sgap-j))
			MatR[i+L,j+L],err = quad(functionx,-1/2,1/2)
	return MatR
'''
def CalcMat(L,sgap):
	MatR = np.zeros([2*L+1,2*L+1])
	for j in range(-L,L+1):
		def functionx(x):
			return np.sinc(x/sgap-j)
		for i in range(-L,L+1):
			MatR[i+L,j+L],err = quad(functionx,(i-0.5)*sgap,(i+0.5)*sgap)
	return MatR


def ImgAddZo(Img,M):
	Half_Mag = int(M/2)
	Img_Mag = np.zeros([M*Img.shape[0],M*Img.shape[1]])
	Img_Mag[Half_Mag*Img.shape[0]:(Half_Mag+1)*Img.shape[0],Half_Mag*Img.shape[1]:(Half_Mag+1)*Img.shape[1]] = Img
	return Img_Mag


def ImgCut(Img,Pos,len):
	return 0


'''
img_avg = cv2.imread('samavg.png',cv2.IMREAD_GRAYSCALE)
img_pix = cv2.imread('sampix.png',cv2.IMREAD_GRAYSCALE)
img_avg_f = img_avg.astype(float)
img_pix_f = img_pix.astype(float)
'''
img_avg = np.load('samavg.npy')
img_pix = np.load('sampix.npy')
inv_gauss = np.load('inv_gauss.npy')
img_avg_M = ImgAddZo(img_avg,5)
img_pix_M = ImgAddZo(img_pix,5)
L = int(img_avg_M.shape[0]/2)
Mag = 5


#print([img_avg_f.dtype,img_pix_f.dtype])

sgap = 5
matZ2 = CalcMat(L,sgap)
inv_matZ2 = inv(matZ2)
inv_img_avg = np.dot(inv_matZ2,np.dot(img_avg_M,inv_matZ2))*sgap**2
#inv_img_avg = np.dot(inv_matZ2,np.dot(inv_img_avg_f,inv_matZ2))*sgap**2

'''
img_pix_i = img_pix/inv_gauss
img_avg_i = img_avg/inv_gauss
inv_img_avg_i = inv_img_avg/inv_gauss

err_img = inv_img_avg_i - img_pix_i
err_img1 = inv_img_avg_i - img_avg_i
'''
err_img = inv_img_avg - img_pix_M
err_img1 = inv_img_avg - img_avg_M

fig, ax = plt.subplots(2,3,figsize=(12,6),constrained_layout = True)
im1 = ax[0][0].imshow(img_avg_M)
im2 = ax[0][1].imshow(img_pix_M)
im3 = ax[0][2].imshow(inv_img_avg)
im4 = ax[1][0].imshow(err_img1)
im5 = ax[1][1].imshow(err_img)
im6 = ax[1][2].imshow(img_avg_M)

fig.colorbar(im1,ax = ax[0][0])
ax[0][0].set_title('Integrated Sampled Image')
ax[0][0].text(-5,-1.5,'(a)',fontsize=12)

fig.colorbar(im2,ax = ax[0][1])
ax[0][1].set_title('Pixel Sampled Signal')
ax[0][1].text(-5,-1.5,'(b)',fontsize=12)

fig.colorbar(im3,ax = ax[0][2])
ax[0][2].set_title('Reconstructed Pixel Sampled Signal')
ax[0][2].text(-5,-1.5,'(c)',fontsize=12)

fig.colorbar(im4,ax = ax[1][0])
ax[1][0].set_title('R-I')
ax[1][0].text(-5,-1.5,'(d)',fontsize=12)

fig.colorbar(im5,ax = ax[1][1])
ax[1][1].set_title('R-P')
ax[1][1].text(-5,-1.5,'(e)',fontsize=12)

fig.colorbar(im6,ax = ax[1][2])
ax[1][2].set_title('I-P')
ax[1][2].text(-5,-1.5,'(f)',fontsize=12)

plt.savefig('img_rcr3.png',dpi=300)

