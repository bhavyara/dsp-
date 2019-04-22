#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:21:14 2019

@author: aravind
"""
import numpy as np
def conv(A,B):
    l1=len(A)
    l2=len(B)
    l=l1+l2-1
    a=np.zeros(l-l1)
    b=np.zeros(l-l2)
    A=np.append(A,a)
    B=np.append(B,b)
    C=np.zeros(l)
    for i in range(0,l,1):
        for j in range(0,l,1):
            C[i]+=A[j]*B[i-j]
    return C
def rev(A):
    l=len(A)
    R=np.zeros(l)
    for i in range(0,l,1):
        R[-(i+1)]=A[i]
    return R
        