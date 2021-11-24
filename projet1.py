import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
# -*- coding: utf-8 -*-


#_______________Projet OPT201____________

#2.
def c(z,L,a,b):
    n=np.size(z)[0]/2
    x=[0]+z[0:n,:]+[a]
    y=[0]+z[n:,:]+[b]
    c=np.zeros((n+1,1))
    for i in range (n+1):
        l=(x[i+1]-x[i])**2+(y[i+1]-y[i])**2
        c[i]=l-L**2
    return c
    
#3.
def cost(z):
    n=np.size(z)[0]/2
    y=z[n:,:]
    S=0
    for i in range (n):
        S=S+y[i]
    return S



