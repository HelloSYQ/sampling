#!/usr/bin/python3

import numpy as np

s = input()
t = input()
q = int(input())

ij = np.zeros((2,q),dtype = int)
for k in range(0,q):
	i_j = input().split()
	ij[0][k] = int(i_j[0])
	ij[1][k] = int(i_j[1])

for k in range(0,q):
	max_len = 0
	for m in range(ij[0][k]-1,len(s)):
		if (m != len(s) - 1):
			for n in range(ij[1][k]-1,len(t)):
				if s[m]<t[n]:
					tmp = len(s)-m+len(t)-n
					if (tmp > max_len):
						max_len = tmp
		else:
			tmp = len(t)-ij[1][k]+1
			if (tmp > max_len):
				max_len = tmp
	print(max_len)



