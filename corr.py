#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:28:44 2019

@author: vamsi
"""


import numpy as np
def convolute(x,h):
	n1 = len(x)
	n2 = len(h)
	y = []
	for n in range(n1+n2-1):
		sum = 0 
		for k in range(n1):
			if ((n-k>=0)&(n-k<=n2-1)):
				sum = sum +(x[k]*h[n-k])
		y = np.append(y,sum)
	return y

def time_rev(h):
	l = len(h)
	hr = []
	for i in range(l):
		 hr=np.append(hr,h[l-i-1])
	return hr

def corr(x,h):
	hr = time_rev(h)
	y = convolute(x,hr)
	return y
	
	
	
x = input('x1=')
h = input('x2=')
y2 = corr(x,h)
print(y2)

