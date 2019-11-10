# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:04:39 2019

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

w = np.ones(num)

stepcount = 20

c1 = "FBB03B"
c2 = "D4145A"
colors = np.sqrt(np.linspace([int(c1[i:i+2], 16)**2 for i in (0, 2, 4)],
                             [int(c2[i:i+2], 16)**2 for i in (0, 2, 4)],
                             stepcount))/255

for i in range(stepcount):
    
    x = geodat.constrainedWeightedRegression(P, L, w)
    
    d = (P @ x)**2
    
    w = 1 / (d + 1)
    
    A, B, C, D = x
    
    m = -1/(2*A) * np.array((B, C)).reshape((2,1))
    r = np.sqrt(abs(B**2 + C**2 - 4*A*D)/(4*A**2))
    
    t = np.linspace(0, 2*np.pi, 100)
    c = m + r * np.stack((np.cos(t), np.sin(t)))
    
    plt.plot(*c, c = colors[i])

#Plotting

plt.axis("equal")

plt.plot(*p.T, ".")

