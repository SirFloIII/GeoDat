# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:59:20 2019

@author: Flo'
"""
################################################
#    ___       _ __             __     __      #
#   / _ )___  (_) /__ _______  / /__ _/ /____  #
#  / _  / _ \/ / / -_) __/ _ \/ / _ `/ __/ -_) #
# /____/\___/_/_/\__/_/ / .__/_/\_,_/\__/\__/  #
#                      /_/                     #
################################################

import numpy as np

url = "https://www.geometrie.tuwien.ac.at/mueller/files/daten/ausgleichsebene.txt"
filename = url.split("/")[-1]

try:
    x = np.loadtxt(filename)
except:
    import urllib.request
    
    urllib.request.urlretrieve(url, filename)
    x = np.loadtxt(filename)
    
n = len(x)

##################################
#  ________                _     #
# /_  __/ /  ___ ___  ____(_)__  #
#  / / / _ \/ -_) _ \/ __/ / -_) #
# /_/ /_//_/\__/\___/_/ /_/\__/  #
#                                #
##################################

"""
y = x - mean(x)

minimiere f(n) := n.T @ sum(y @ y.T) @ n
                              := C

g(n) := ||n|| - 1
                              
L' = C*n - λ*n

C*n = λ*n
"""

###############################
#    ___                 _    #
#   / _ \_______ ___ __ (_)__ #
#  / ___/ __/ _ `/\ \ // (_-< #
# /_/  /_/  \_,_//_\_\/_/___/ #
#                             #
###############################

d = np.mean(x, axis = 0)

y = x - d

C = y.T @ y

ew, ev = np.linalg.eig(C)

n = min(zip(ew, ev), key = lambda x:x[0])[1]

n = n/np.linalg.norm(n)








