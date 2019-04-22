#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:51:22 2019

@author: aravind
"""

import numpy as np
import matplotlib.pyplot as plt
from conv import conv,rev
l1=input("length of first signal:")
l2=input("length of first signal:")
l=l1+l2-1
A=np.zeros(l1)
B=np.zeros(l2)
for i in range(0,l1,1):
    A[i]=input("enter an element for signal 1:")
for i in range(0,l2,1):
    B[i]=input("enter an element for signal 2:")
R=rev(B)
C=conv(A,R)
plt.stem(C)
plt.show()