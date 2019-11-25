# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 02:52:30 2019

@author: Flo
"""

import geodat
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

p = geodat.getPoints("points.txt")
n = geodat.getPoints("normals.txt")
num = len(p)

n_bar = np.cross(p,n)
n_combined = [ [*n[i],*n_bar[i]] for i in range(len(n))]
print(n_combined[0])

def minSquare(x):
    d = np.mean(x, axis = 0)
    y = x - d
    C = y.T @ y
    ew, ev = np.linalg.eig(C)
    n = min(zip(ew, ev), key = lambda x:x[0])[1]
    return n/np.linalg.norm(n)

c = [0,0,0]
c_bar = [0,0,0]

c[0],c[1],c[2],c_bar[0],c_bar[1],c_bar[2] = minSquare(n_combined)

print(c)
print(c_bar)

# (c cbar)^t Q (= sum (n nbar)^t (n nbar)) (c cbar)
# <c,c_bar>/<c,c> = p
# (g, gbar) = (c, cbar - p c), dh richtungsvektor = g = c

#plot in 3d
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')

ax.set_zlim(-4, 4)

ax.scatter(*p.T, s=1, c = (n+1)/2)

#von "oben"
ax = fig.add_subplot(222)
ax.axis("equal")

ax.scatter(p[:,0], p[:, 1], s = 1, c = (n+1)/2)

#postuliere: drehachse ist z achse durch den nullpunkt
#drehe punkte in die x-z achse und färbe nach drehwinkel ein:

ax = fig.add_subplot(223)
ax.axis("equal")

phi = np.arctan2(p[:,0], p[:,1])

c = np.cos(phi)
s = np.sin(phi)

z = np.zeros(num)
o = np.ones(num)

A = np.array(([ c, s, z],
              [-s, c, z],
              [ z, z, o])).T
              
q = np.array([a@s for a,s in zip(A, p)])
ax.scatter(q[:,1], q[:, 2], s = 1, c = phi)

#errate schraubanteil:

ax = fig.add_subplot(224)
ax.axis("equal")

c = -0.5

ax.scatter(q[:,1], q[:, 2] - c*phi, s = 1, c = phi)









