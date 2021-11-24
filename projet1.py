import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
# -*- coding: utf-8 -*-


#_______________Projet OPT201____________

#2.

a=1
b=1
L=1

def c(z):
    n=np.size(z)[0]/2
    x=[0]+z[0:n,:]+[a]
    y=[0]+z[n:,:]+[b]
    c=np.zeros((n+1,1))
    for i in range (n+1):
        l=(x[i+1]-x[i])**2+(y[i+1]-y[i])**2
        c[i,0]=l-L**2
    return c
    
#3.
def cost(z):
    n=np.size(z)[0]/2
    y=z[n:,:]
    S=0
    for i in range (n):
        S=S+y[i]
    return S


#4.
def lag(z,lambda):
    n=np.size(z)[0]/2
    e=np.zeros((2*n,1))
    for i in range (n):
        e[i+n,0]=1
    return np.transpose(e)*z + np.transpose(lambda)*c(z)
    
