#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def Image2Dto1D(img_src):
	img1d = np.reshape(img_src,(-1,1),order='F')
	print(img1d.shape)
	return img1d


def SampMat4Dto1D(samp_mat):
	samp_mat2d = np.reshape(samp_mat,(-1,4),order='F')
	return samp_mat2d

def CalcSampMat(M,N):
	return 0





#**--main--**
a = np.array([[[[1,2],[1,2]],[[1,2],[1,2]]],[[[1,2],[1,2]],[[1,2],[1,2]]]])
a_r = SampMat4Dto1D(a)
print(a_r)
