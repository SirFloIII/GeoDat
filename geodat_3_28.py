# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:10:38 2019

@author: Flo
"""

import numpy as np

"""
phi1 = x² + 3y² + 2z² + 2xy - 1 == 0

phi2 = x² - 3y² + 2z² + 2xy - 1 == 0

f = x² + 2*y² + z² - 2yz -> min
"""

G1 = np.array(([ 1,  1,  0],
               [ 1,  3,  0],
               [ 0,  0,  2]))

G2 = np.array(([ 1,  1,  0],
               [ 1, -3,  0],
               [ 0,  0,  2]))

A  = np.array(([ 1,  0,  0],
               [ 0,  2, -1],
               [ 0, -1,  1]))

"""
f = x.T * A * x

g = x.T * G * x - 1 = 0

L(x, λ) = x.T*A*x - λ * (x.T*G*x - 1)

∇L = 0 =>

A*x == λ*G*x
oder (wenn G invertierbar ist)
G^-1 * A * x == λ*x

löse verallgemeinertes Eigenwertproblem
minimum x* ist normierter EV zum kleinsten EW λ
(normiert im Sinne von x*.T*G*x* = 1)
"""

#import scipy as sp
#ew, ev = sp.linalg.eig(A, G1)


eigenwerte, eigenvektoren = np.linalg.eig(np.linalg.inv(G1).dot(A))

x = min(zip(eigenwerte, eigenvektoren.T), key = lambda x:x[0])[1]

x = x/np.sqrt((x.dot(G1).dot(x)))

print("\nphi(x) =", x.dot(G1).dot(x) - 1)
print("\nf(x) =", x.dot(A).dot(x))
print("\nx =", x)