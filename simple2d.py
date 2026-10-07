#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from numpy.linalg import inv

def CalcMat(L):
	MatR = np.zeros([2*L+1,2*L+1])
	for j in range(-L,L+1):
		def function(x):
			return np.sinc(x-j)
		for i in range(-L,L+1):
			MatR[i+L,j+L],err = quad(function,i-0.5,i+0.5)
	return MatR


m = CalcMat(10)
print(m)
m_inv = inv(m)
print(inv(m))


Time('2021-1-18 00:00:00'),Time('2021-1-18 02:00:00'),Time('2021-1-18 04:00:00'),Time('2021-1-18 06:00:00'),Time('2021-1-18 08:00:00'),Time('2021-1-18 10:00:00'),\
Time('2021-1-18 12:00:00'),Time('2021-1-18 14:00:00'),Time('2021-1-18 16:00:00'),Time('2021-1-18 18:00:00'),Time('2021-1-18 20:00:00'),Time('2021-1-18 22:00:00'),\
