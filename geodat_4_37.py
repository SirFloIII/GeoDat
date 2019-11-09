# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:40:58 2019

@author: Flo
"""

import geodat
import numpy as np

import matplotlib.pyplot as plt

p = geodat.getPoints("kreis.txt")
num = len(p)


plt.scatter(*p.T, s = 1)
plt.axis("equal")

"""
[Pottmann: Industrial Geometry, S.48ff]

signed distance c(p) = A*(p1² + p2²) + B*p1 + C*p2 + D

with A2² + A3² - 4*A1*A4 = 1    (1)

minimize f(A, B, C, D) = sum_i(c(p_i)²)

let P = (p1² + p2², p1, p2, 1)

let"""

L = np.array(([ 0, 0, 0, -2],
              [ 0, 1, 0,  0],
              [ 0, 0, 1,  0],
              [-2, 0, 0,  0]))

"""be the quatriatic form of the normalization condition (1).

solve general EV problem λ * L * x = P.T * P * x
                                        := K

EV to smallest non-negative EW x = (A, B, C, D) corresponds to best Fit.

m = -1/2A * (B,C), r² = (B²+C² - 4AD) / 4A²
"""

P = np.stack((np.sum(p**2, axis = 1), *p.T, np.ones(num))).T

A, B, C, D = geodat.constrainedWeightedRegression(P, L)

m = -1/(2*A) * np.array((B, C)).reshape((2,1))

r = np.sqrt(abs(B**2 + C**2 - 4*A*D)/(4*A**2))

#Plotting

t = np.linspace(0, 2*np.pi)

x = m + r * np.stack((np.cos(t), np.sin(t)))


plt.plot(*x)






















