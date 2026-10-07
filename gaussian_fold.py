#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.linalg import inv
from scipy.linalg import det


_parula_data = [[0.2081, 0.1663, 0.5292], 
                [0.2116238095, 0.1897809524, 0.5776761905], 
                [0.212252381, 0.2137714286, 0.6269714286], 
                [0.2081, 0.2386, 0.6770857143], 
                [0.1959047619, 0.2644571429, 0.7279], 
                [0.1707285714, 0.2919380952, 0.779247619], 
                [0.1252714286, 0.3242428571, 0.8302714286], 
                [0.0591333333, 0.3598333333, 0.8683333333], 
                [0.0116952381, 0.3875095238, 0.8819571429], 
                [0.0059571429, 0.4086142857, 0.8828428571], 
                [0.0165142857, 0.4266, 0.8786333333], 
                [0.032852381, 0.4430428571, 0.8719571429], 
                [0.0498142857, 0.4585714286, 0.8640571429], 
                [0.0629333333, 0.4736904762, 0.8554380952], 
                [0.0722666667, 0.4886666667, 0.8467], 
                [0.0779428571, 0.5039857143, 0.8383714286], 
                [0.079347619, 0.5200238095, 0.8311809524], 
                [0.0749428571, 0.5375428571, 0.8262714286], 
                [0.0640571429, 0.5569857143, 0.8239571429], 
                [0.0487714286, 0.5772238095, 0.8228285714], 
                [0.0343428571, 0.5965809524, 0.819852381], 
                [0.0265, 0.6137, 0.8135], 
                [0.0238904762, 0.6286619048, 0.8037619048], 
                [0.0230904762, 0.6417857143, 0.7912666667], 
                [0.0227714286, 0.6534857143, 0.7767571429], 
                [0.0266619048, 0.6641952381, 0.7607190476], 
                [0.0383714286, 0.6742714286, 0.743552381], 
                [0.0589714286, 0.6837571429, 0.7253857143], 
                [0.0843, 0.6928333333, 0.7061666667], 
                [0.1132952381, 0.7015, 0.6858571429], 
                [0.1452714286, 0.7097571429, 0.6646285714], 
                [0.1801333333, 0.7176571429, 0.6424333333], 
                [0.2178285714, 0.7250428571, 0.6192619048], 
                [0.2586428571, 0.7317142857, 0.5954285714], 
                [0.3021714286, 0.7376047619, 0.5711857143], 
                [0.3481666667, 0.7424333333, 0.5472666667], 
                [0.3952571429, 0.7459, 0.5244428571], 
                [0.4420095238, 0.7480809524, 0.5033142857], 
                [0.4871238095, 0.7490619048, 0.4839761905], 
                [0.5300285714, 0.7491142857, 0.4661142857], 
                [0.5708571429, 0.7485190476, 0.4493904762],
                [0.609852381, 0.7473142857, 0.4336857143], 
                [0.6473, 0.7456, 0.4188], 
                [0.6834190476, 0.7434761905, 0.4044333333], 
                [0.7184095238, 0.7411333333, 0.3904761905], 
                [0.7524857143, 0.7384, 0.3768142857], 
                [0.7858428571, 0.7355666667, 0.3632714286], 
                [0.8185047619, 0.7327333333, 0.3497904762], 
                [0.8506571429, 0.7299, 0.3360285714], 
                [0.8824333333, 0.7274333333, 0.3217], 
                [0.9139333333, 0.7257857143, 0.3062761905], 
                [0.9449571429, 0.7261142857, 0.2886428571], 
                [0.9738952381, 0.7313952381, 0.266647619], 
                [0.9937714286, 0.7454571429, 0.240347619], 
                [0.9990428571, 0.7653142857, 0.2164142857], 
                [0.9955333333, 0.7860571429, 0.196652381], 
                [0.988, 0.8066, 0.1793666667], 
                [0.9788571429, 0.8271428571, 0.1633142857], 
                [0.9697, 0.8481380952, 0.147452381], 
                [0.9625857143, 0.8705142857, 0.1309], 
                [0.9588714286, 0.8949, 0.1132428571], 
                [0.9598238095, 0.9218333333, 0.0948380952], 
                [0.9661, 0.9514428571, 0.0755333333], 
                [0.9763, 0.9831, 0.0538]]

parula = ListedColormap(_parula_data)

def CalcMat(L):
	MatR = np.zeros([2*L+1,2*L+1])
	for j in range(-L,L+1):
		def functionx(x):
			return np.sinc(x-j)
		for i in range(-L,L+1):
			MatR[i+L,j+L],err = quad(functionx,i-0.5,i+0.5)
	return MatR


# draw Gaussian Plot and Folded Gaussian Plot

# Calculate Guassian Plot
L = 20
X = np.arange(-L, L+1, 1.0)
Y = np.arange(-L, L+1, 1.0)
X1, Y1 = np.meshgrid(X, Y)
R = (X1**2 + Y1**2)
R1 = (X1-5)**2 + (Y1-5)**2
R2 = (X1-(4e-2*X1**2)+(2e-2*Y1**2))**2+(Y1+(6e-2*X1**2)-(3e-2*Y1**2))**2
sigma = 1.5

Z1 = np.exp(-R/(2*sigma**2))+0.2*np.exp(-R1/(2*sigma**2))
'''
Z1 = np.exp(-R/(2*sigma**2))
Z4 = np.exp(-R2/(2*sigma**2))
'''
# Calculate folded Guassian Plot

def function(x):
	return np.exp(-x**2/(2*sigma**2))+0.2*np.exp(-(x-5)**2/(2*sigma**2))


f = lambda x,y :np.exp(-(x**2+y**2)/(2*sigma**2))+0.2*np.exp(-((x-5)**2+(y-5)**2)/(2*sigma**2))

Z2 = np.zeros([2*L+1,2*L+1])
tempZ2 = np.zeros([2*L+1,1])
'''
for i in range(-L,L+1):
	tempZ2[i+L],err = quad(function,i-0.5,i+0.5)
'''

for i in range(2*L+1):
	for j in range(2*L+1):
		Z2[i,j], err = dblquad(f, j-L-0.5, j-L+0.5, lambda g : i-L-0.5, lambda h : i-L+0.5)	

Z3 = Z1-Z2

# calculate the recovered Z1
matZ2 = CalcMat(L)
inv_matZ2 = inv(matZ2)
temp_Z2 = np.dot(inv_matZ2,Z2)
reverse_Z2 = np.dot(temp_Z2,inv_matZ2)
errZ2 = reverse_Z2-Z1


fig, ax = plt.subplots(2,3,figsize=(12,6),constrained_layout = True)
im1 = ax[0][0].imshow(Z1, cmap = 'Wistia')
im2 = ax[0][1].imshow(Z2, cmap = 'Wistia')
im3 = ax[0][2].imshow(reverse_Z2, cmap = 'Wistia')
im4 = ax[1][0].imshow(Z3, cmap = 'Wistia')
im5 = ax[1][1].imshow(errZ2,cmap = 'Wistia')
im6 = ax[1][2].imshow(matZ2,cmap = 'Wistia')

fig.colorbar(im1,ax = ax[0][0])
ax[0][0].set_title('Impulse Sampled Signal')
ax[0][0].text(-5,-1.5,'(a)',fontsize=12)
fig.colorbar(im2,ax = ax[0][1])
ax[0][1].set_title('Integrated Sampled Signal')
ax[0][1].text(-5,-1.5,'(b)',fontsize=12)
fig.colorbar(im3,ax = ax[0][2])
ax[0][2].set_title('Reconstructed Impulse Signal')
ax[0][2].text(-5,-1.5,'(c)',fontsize=12)
fig.colorbar(im4,ax = ax[1][0])
ax[1][0].set_title('Error Image 1')
ax[1][0].text(-5,-1.5,'(d)',fontsize=12)
fig.colorbar(im5,ax = ax[1][1])
ax[1][1].set_title('Error Image 2')
ax[1][1].text(-5,-1.5,'(e)',fontsize=12)
fig.colorbar(im6,ax = ax[1][2])
ax[1][2].set_title('R MATRIX')
ax[1][2].text(-5,-1.5,'(f)',fontsize=12)
plt.savefig('GaussianFold.png',dpi=300)
#plt.show()
'''

fig, ax = plt.subplots(1,2,figsize=(6,2),constrained_layout = True)
im1 = ax[0].imshow(Z1,cmap = parula)
im2 = ax[1].imshow(Z4,cmap = parula)


fig.colorbar(im1,ax = ax[0])
ax[0].set_title('Non-Distorted PSF')
ax[0].text(-12,-1.5,'(a)',fontsize=12)
fig.colorbar(im2,ax = ax[1])
ax[1].set_title('Distorted PSF')
ax[1].text(-12,-1.5,'(b)',fontsize=12)


plt.savefig('GaussianDist.png',dpi=300)
'''
