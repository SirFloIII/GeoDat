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

url = "https://www.geometrie.tuwien.ac.at/mueller/files/daten/quadr-rot.txt"
filename = url.split("/")[-1]

try:
    x = np.loadtxt(filename)
except:
    import urllib.request
    
    urllib.request.urlretrieve(url, filename)
    x = np.loadtxt(filename)
    
n = len(x)

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


#Plotting

#richtungsvektor der Ausgleichsgerade
r = (n[::-1]*(1,-1)).reshape((2,1))
t = np.linspace(-5,10).reshape((1,-1))
#punkte auf der gerade
g = (d*n).reshape((2,1))+t*r

plt.axis("equal")
plt.scatter(x[:,0], x[:,1])
plt.plot(g[0], g[1])
plt.scatter(*z.T)
