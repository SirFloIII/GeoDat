# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:32:33 2019

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

url = "https://www.geometrie.tuwien.ac.at/mueller/files/daten/flaeche.txt"
filename = url.split("/")[-1]

try:
    x = np.loadtxt(filename)
except:
    import urllib.request
    
    urllib.request.urlretrieve(url, filename)
    x = np.loadtxt(filename)
    
n = len(x)

#from past import deppates beispiel von letztns