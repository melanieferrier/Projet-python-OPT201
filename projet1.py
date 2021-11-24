import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp
# -*- coding: utf-8 -*-


#_______________Projet OPT201____________

#2.

L=2

def c(z):
    n=np.size(z)[0]/2
    x=[0]+z[0:n,:]
    y=[0]+z[n:,:]
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


#5.
def dzlag(z,lambda):
    n=np.size(z)[0]/2
    e=np.zeros((2*n,1))
    for i in range (n):
        e[i+n,0]=1
    x=[0]+z[:n,:]
    y=[0]+z[n:,:]
    dzc=np.zeros((2*n,n+1))
    for i in range(n):
        for j in range(n+1):
            dzc[i,j]=2*(x[i+1]-x[i])
            dzc[i+n,j]=2*(y[i+1]-y[i])
    return e + np.transpose(dzc)*lambda
