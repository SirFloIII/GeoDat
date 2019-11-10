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


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_zlim(-4, 4)

ax.scatter(*p.T, s=1, c = (n+1)/2)

