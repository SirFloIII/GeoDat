# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:06:20 2019

@author: User
"""

################################################
#    ___       _ __             __     __      #
#   / _ )___  (_) /__ _______  / /__ _/ /____  #
#  / _  / _ \/ / / -_) __/ _ \/ / _ `/ __/ -_) #
# /____/\___/_/_/\__/_/ / .__/_/\_,_/\__/\__/  #
#                      /_/                     #
################################################

import numpy as np
from matplotlib import pyplot as plt

import geodat

x = geodat.getPoints("quadr-rot.txt")
m = len(x)

#Theorie: siehe 30)

#Praxis:

#Ausgleichsgerade:

d = np.mean(x, axis = 0)

y = x - d

C = y.T @ y

ew, ev = np.linalg.eig(C)

n = min(zip(ew, ev), key = lambda x:x[0])[1]

n = n/np.linalg.norm(n)

#Drehung, sodass Ausgleichsgerade horizontal liegt.

# Orthogonale Drehmatrix, die n auf (0,1) abbildet:
A = np.array(([n[1] , -n[0]],
              [n[0],  -n[1]]))

z = (A@y.T).T

#from past import letze übung
#copypaste ist sicher kein antipattern

A = np.stack((np.ones(m), z[:, 0], z[:, 0]**2)).T

b = z[:, 1]

At = np.linalg.pinv(A)

a0, a1, a2 = At.dot(b)


#####################################
#         __     __  __  _          #
#   ___  / /__  / /_/ /_(_)__  ___ _#
#  / _ \/ / _ \/ __/ __/ / _ \/ _ `/#
# / .__/_/\___/\__/\__/_/_//_/\_, / #
#/_/                         /___/  #
#####################################

#richtungsvektor der Ausgleichsgerade
r = (n[::-1]*(1,-1)).reshape((2,1))
t = np.linspace(-4,10).reshape((1,-1))
#punkte auf der gerade
g = (d*n).reshape((2,1))+t*r

plt.axis("equal")



plt.scatter(*x.T, marker = ".")

plt.plot(g[0], g[1])

plt.scatter(*z.T, marker = ".")


xp = np.linspace(min(z[:, 0]), max(z[:, 0]))

yp = a0 + a1*xp + a2*xp**2

plt.plot(xp, yp, color = "tab:red")

