#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:38:42 2019

@author: aravind
"""
import numpy as np
import matplotlib.pyplot as plt
f=input("enter frequenncy")
n=np.linspace(0,10,1000)
x=np.sin(2*np.pi*(f)*n)
plt.plot(n,x)
plt.title("sine wave")
plt.xlabel("------------>time")
plt.ylabel("amplitude")

plt.show()
