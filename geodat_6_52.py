# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:31:32 2019

@author: Flo
"""

import numpy as np
import matplotlib.pyplot as plt

import geodat

P = np.array([[ 0, 0],
              [ 0, 1],
              [-1, 1],
              [-1,-1],
              [ 1,-1],
              [ 1, 0]])

Q = np.array([[ 0, 0],
              [ 0, 1],
              [-2, 1],
              [-2,-1],
              [ 2,-1],
              [ 2, 0]])


S = np.array([[ 0, 0],
              [ 0, 1],
              [-1, 1],
              [-2,-2],
              [ 1,-1],
              [ 1, 0]])


"""
minimize f(A, a) = sum (w_i * ||(a,A)*(1,p_i) - q_i||²)


(1,p) * (a,A) = q
 :=M    :=x     :=b
n,3      3,2    n,2
"""


A, a = geodat.registration(P,S)

plt.axis("equal")

plt.scatter(*(P@A + a).T)
plt.scatter(*S.T)

plt.show()



































