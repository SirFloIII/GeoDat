# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:47:32 2019

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
import geodat_2_20

url = "http://www.geometrie.tuwien.ac.at/ig/mueller/files/daten/ausgleichsparabel.txt"
filename = url.split("/")[-1]

try:
    p = np.loadtxt(filename)
except OSError:
    import urllib.request

    urllib.request.urlretrieve(url, filename)
    p = np.loadtxt(filename)

p, _ = geodat_2_20.umgebung(p, (0,0), 2)

n = len(p)

################################
# ________                _    #
#/_  __/ /  ___ ___  ____(_)__ #
# / / / _ \/ -_) _ \/ __/ / -_)#
#/_/ /_//_/\__/\___/_/ /_/\__/ #
#                              #
################################
#
# miniere sum(||a0 + a1 * x + a2*x² - y_i||_2)
# mit (x, y) = p und a frei
#
# (1, x, x²) * (a0, a1, a2) = y
#  := A            := x      := b
#
# A*x = b nicht exakt lösbar, da überbestimmt
#
# nach 12.9.6 in der orangenen Bibel suche pseudoinverse für A,
# und nicht nur irgendeine sondern moore penrose inverse A^†
#
# x := A^† * b ist lösung des minimierungsproblems.
#
# danke an Prof. Havlicek
#
##############################
#   ___                 _    #
#  / _ \_______ ___ __ (_)__ #
# / ___/ __/ _ `/\ \ // (_-< #
#/_/  /_/  \_,_//_\_\/_/___/ #
#                            #
##############################

A = np.stack((np.ones(n), p[:, 0], p[:, 0]**2)).T

b = p[:, 1]

At = np.linalg.pinv(A)

a0, a1, a2 = At.dot(b)

#####################################
#         __     __  __  _          #
#   ___  / /__  / /_/ /_(_)__  ___ _#
#  / _ \/ / _ \/ __/ __/ / _ \/ _ `/#
# / .__/_/\___/\__/\__/_/_//_/\_, / #
#/_/                         /___/  #
#####################################

x = np.linspace(min(p[:, 0]), max(p[:, 0]))

y = a0 + a1*x + a2*x**2

plt.scatter(p[:,0], p[:,1], marker = ".", color = "tab:blue")

plt.plot(x, y, color = "tab:red")


































