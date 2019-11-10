from geodat import *
import numpy as np
import random
from math import sqrt
import matplotlib.pyplot as plt

################
#### DEFINE ####
################

def circDist(p,R,c):
    return abs(np.sqrt((p[0]-c[0])**2 + (p[1]-c[1])**2)-R)

def circle(p1,p2,p3):
    
    s12 = (p1[0]**2 + p1[1]**2 - p2[0]**2 + p2[1]**2) / 2 # slope of 12
    s23 = (p2[0]**2 + p2[1]**2 - p3[0]**2 - p3[1]**2) / 2 # slope of 23
    det = np.linalg.det([[p1[0] - p2[0], p2[0] - p3[0]] ,
                        [ p1[1] - p2[1], p2[1] - p3[1]]])

    if abs(det) < 1.0e-6: # points on a line
        return (None, np.inf)

    # center of circle
    cx = (s12*(p2[1] - p3[1]) - s23*(p1[1] - p2[1])) / det
    cy = (s23*(p1[0] - p2[0]) - s12*(p2[0] - p3[0])) / det

    radius = np.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    return ((cx, cy), radius)

def RANSAC(points, iters = 100, eps = 0.01):
    xc = np.mean(points[:,0])
    yc = np.mean(points[:,1])
    k = 0
    for i in range(iters):
        ID = random.sample(range(len(points)),3)
        center_estimate = xc, yc
        center, Rnew = circle(*[points[i] for i in ID])# estimate circle from 3 points
        if center == None: # points are on a line
            break
        xc, yc = center
        knew = sum(circDist(p,Rnew,center) < eps for p in points) # sum/count points with distance < eps
        if knew > k:
            k = knew
            R = Rnew
            c = center
    if k == 0: # points were always on a line
        return (0,0),0
    return c, R

###################
#### CALCULATE ####
###################

points = getPoints("https://www.geometrie.tuwien.ac.at/ig/mueller/files/daten/kreis1.txt")

circ = RANSAC(points)

##############
#### PLOT ####
##############

circle = plt.Circle(circ[0], circ[1], color='yellow', fill=False)

fig, ax = plt.subplots()
ax.add_artist(circle)

ax.scatter(*circ[0],color='red')
ax.scatter(*points.T)
ax.grid(color='lightgray',linestyle='--')
plt.axis("equal")
plt.show()
