# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:45:03 2019

@author: Flo
"""

##############################################
#   ___       _ __             __     __     #
#  / _ )___  (_) /__ _______  / /__ _/ /____ #
# / _  / _ \/ / / -_) __/ _ \/ / _ `/ __/ -_)#
#/____/\___/_/_/\__/_/ / .__/_/\_,_/\__/\__/ #
#                     /_/                    #
##############################################


import numpy as np
from matplotlib import pyplot as plt

url = "http://www.geometrie.tuwien.ac.at/ig/mueller/files/daten/ausgleichsgerade.txt"
filename = url.split("/")[-1]

try:
    p = np.loadtxt(filename)
except OSError:
    import urllib.request

    urllib.request.urlretrieve(url, filename)
    p = np.loadtxt(filename)

n = len(p)

################################
# ________                _    #
#/_  __/ /  ___ ___  ____(_)__ #
# / / / _ \/ -_) _ \/ __/ / -_)#
#/_/ /_//_/\__/\___/_/ /_/\__/ #
#                              #
################################

"""
miniere sum(||k*x_i + d - y_i||_2^2) mit x, y = p und k, d frei

(1, x) * (d, k) = y
 := A     := x   := b

A*x = b nicht exakt lösbar, da überbestimmt

nach 12.9.6 in der orangenen Bibel suche pseudoinverse für A,
und nicht nur irgendeine sondern moore penrose inverse A^†

x := A^† * b ist lösung des minimierungsproblems.

danke Prof. Havlicek
"""

##############################
#   ___                 _    #
#  / _ \_______ ___ __ (_)__ #
# / ___/ __/ _ `/\ \ // (_-< #
#/_/  /_/  \_,_//_\_\/_/___/ #
#                            #
##############################

A = np.stack((np.ones(n), p[:, 0])).T

b = p[:, 1]

At = np.linalg.pinv(A)

d, k = At.dot(b)

#####################################
#         __     __  __  _          #
#   ___  / /__  / /_/ /_(_)__  ___ _#
#  / _ \/ / _ \/ __/ __/ / _ \/ _ `/#
# / .__/_/\___/\__/\__/_/_//_/\_, / #
#/_/                         /___/  #
#####################################

x = np.linspace(min(p[:, 0]), max(p[:, 0]))

y = k*x + d

plt.scatter(p[:,0], p[:,1], marker = ".", color = "tab:blue")

plt.plot(x, y, color = "tab:red")

plt.show()