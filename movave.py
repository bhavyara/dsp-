#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:39:43 2019

@author: aravind
"""

#python program to implement moving average system
import numpy as np
import matplotlib.pyplot as plt
n1=np.linspace(0,20,2000)
n2=np.linspace(0,20,2000)
x=5*np.sin(2*np.pi*200*n2)
no=np.sin(2*np.pi*6000*n1)
x1=x+no
fig=plt.figure() 
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
p=input("order of moving average system: ")
p=float(p)
y=np.zeros(2000)
for i in range(0,2000,1):
    j=i
    c=0
    while (j>=0 & c<=p):
        y[i]+=x1[j]
        j=j-1
        c+=1
    y[i]=y[i]/p
ax1.plot(n1,x)
ax2.plot(n1,x1)
ax3.plot(n1,y)
plt.show()