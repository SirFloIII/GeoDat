# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:40:06 2019

@author: Flo
"""

import urllib.request
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def umgebung(p, q, eps):
    d = p.shape[1]
    q = np.array(q).reshape((1,d))
    close = np.linalg.norm(p-q, axis = 1) < eps
    return p[close], close

if __name__ == "__main__":
    
    url = "http://www.geometrie.tuwien.ac.at/ig/mueller/files/daten/punktwolke1.txt"
    filename = url.split("/")[-1]
    
    try:
        p = np.loadtxt(filename)
    except:
        urllib.request.urlretrieve(url, filename)
        p = np.loadtxt(filename)
    
    
    pp, close = umgebung(p, p[500], 1)
    
    color = ["r" if c else "b" for c in close]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_zlim(-4, 4)
    
    ax.scatter(p[:, 0], p[:, 1], p[:, 2],
                       s=1, c = color)
    
    plt.show()