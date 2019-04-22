#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:26:45 2019

@author: aravind
"""

import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(0,10,10)
x=np.sin(2*np.pi*n)
fig=plt.figure() 
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.stem(n,x)
y=np.zeros(10)
for i in range(0,10,1):
    j=i
    while j>=0:
        y[i]+=x[j]
        j=j-1
ax2.stem(n,y)
plt.show()