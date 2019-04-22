#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:29:26 2019

@author: aravind
"""
#dft
import numpy as np
import matplotlib.pyplot as plt
import cmath as c
import scipy.io.wavfile as wav
fig=plt.figure()      #creating subplots
plt.subplots_adjust(left=0.125,right=0.9,bottom=0.1,top=0.9,wspace=0.5,hspace=0.8)#adjusting size of the subplots
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)
j=c.sqrt(-1)
n=np.linspace(0,100,200)
x=np.sin(2*np.pi*(20.0/100.0)*n)
#x=[1,2,3,4,5]
#fs,x=wav.read("hello.wav")

X=[]
A=[]
p=[]
for k in range(0,len(x),1):
    a=0
    for i in range(0,len(x),1):
        a+=x[i]*np.exp((-j)*2*(np.pi)*k*i/len(x))
    X.append(a)
    A.append(np.abs(a))
    p.append(np.angle(a))
print X
ax1.stem(X)
ax2.stem(A)
ax3.stem(p)
plt.show()