#!/usr/bin/python3

import numpy as np

def Find_A(mat,a):
	for i in range(mat.shape[0]):
		for j in range(mat.shape[1]):
			if mat[i][j] == a:
				return(i,j)
	return(-1,-1)

nm = input().split()
w = input().split()

n = int(nm[0])
m = int(nm[1])
w = list(map(int,w))

w_minus = np.zeros((len(w),len(w)))

for i in range(0,len(w)):
	for j in range(0,len(w)):
		w_minus[i,j] = abs(w[i]-w[j])

a = np.zeros(m)
for i in range(0,m):
	a[i] = int(input())

for i in range(0,m):
	preprint = Find_A(w_minus,a[i])
	if preprint[0] == -1 and preprint[1] == -1:
		print(-1,-1)
	else:
		print(w[preprint[0]],w[preprint[1]])


