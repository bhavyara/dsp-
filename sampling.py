#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:10:35 2019

@author: aravind
"""
import numpy as np
import matplotlib.pyplot as plt
f=input("enter frequency of sine")
f=float(f)
fs=input("enter sampling frequency")
fs=float(fs)
fig=plt.figure()      #creating subplots
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)#adjusting size of the subplots
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
n1=np.linspace(0,100,20)
n2=np.linspace(0,10,2000)
x=np.sin(2*np.pi*(f/fs)*n1)
y=np.sin(2*np.pi*(f)*n2)
ax2.stem(n1,x)
ax2.set_title("sampled sine wave")
ax2.set_xlabel("----------------->time")
ax2.set_ylabel("amplitude")
ax1.plot(n2,y)
ax1.set_title("sine wave")
ax1.set_xlabel("----------------->time")
ax1.set_ylabel("amplitude")
#plt.plot(n,x)
plt.show()

