# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 02:16:26 2019

@author: Flo
"""

import geodat
import numpy as np

import matplotlib.pyplot as plt

p = geodat.getPoints("kreis1.txt")
num = len(p)

L = np.array(([ 0, 0, 0, -2],
              [ 0, 1, 0,  0],
              [ 0, 0, 1,  0],
              [-2, 0, 0,  0]))

P = np.stack((np.sum(p**2, axis = 1), *p.T, np.ones(num))).T


#percentage of points to keep:
amount = 0.01

trials = 5

delta = 1


bestYetCount = 0

for i in range(trials):
    
    Psub = P[np.random.uniform(size = num) < amount]
    
    x = geodat.constrainedWeightedRegression(Psub, L)
    
    closeCount = sum(np.abs(P @ x) < delta)
    
    if closeCount > bestYetCount:
        bestYetCount = closeCount
        bestX = x
        


#Plotting

A, B, C, D = bestX
    
m = -1/(2*A) * np.array((B, C)).reshape((2,1))
r = np.sqrt(abs(B**2 + C**2 - 4*A*D)/(4*A**2))

t = np.linspace(0, 2*np.pi, 100)
c = m + r * np.stack((np.cos(t), np.sin(t)))

plt.axis("equal")

plt.plot(*p.T, ".")

plt.plot(*c)












