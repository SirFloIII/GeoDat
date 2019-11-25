import numpy as np

import urllib.request
import os

def getPoints(url,back="src"):
 
    if not "https" in url:
        url = os.path.join("https://www.geometrie.tuwien.ac.at/mueller/files/daten/", url)
    
    filename = os.path.join(back, os.path.basename(url))
    if os.path.isfile(filename):
      points = np.loadtxt(filename)
      return points
    
    if not os.path.exists(back):
        os.makedirs(back)
    
    urllib.request.urlretrieve(url, filename)
    points = np.loadtxt(filename)
    return points

def smallestNonNegativeEV(ew, ev):
    #ev gets transposed because of numpy.linalg.eig stupidly
    #returns the eigenvector for ew[i] in ev[:,i] and not in ev[i]   
    return min(zip(ev.T, ew), key = lambda x: np.float("inf") if x[1] < 0 else x[1])[0]

def smallestEV(ew, ev):
    return min(zip(ev.T, ew), key = lambda x: x[1])[0]

def constrainedWeightedRegression(P, L, w = None):
    """
    solve A*x == λ*L*x with Q = w*P and A = Q.T @ Q
    and return smallest nonnegative Eigenvector
    
    ie. solve the constrained weighted Regression
    P ... generalised Vandermonde-Matrix
    L ... quadradic Form aka. Constraint
    """
    
    if np.all(w != None):
        Q = (P.T*w).T
        A = Q.T @ Q
    else:
        A = P.T @ P
    
    if np.linalg.det(L) == 0 :
      #generalised
      import scipy.linalg as spla
      ew, ev = spla.eig(A,L)
    else:
      ew, ev = np.linalg.eig(np.linalg.inv(L) @ A)

    x = smallestNonNegativeEV(ew, ev)
    
    return x/(x.T @ L @ x)
    
#def WeightedRegression(A, b, w):
    #maybe later   
    