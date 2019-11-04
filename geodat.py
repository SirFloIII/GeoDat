import numpy as np

import urllib.request
import os

def getPoints(url,back="src"):
    filename = os.path.join(back,os.path.basename(url))
    if os.path.isfile(filename):
        points = np.loadtxt(filename)
        return points
    if not os.path.exists(back):
        os.makedirs(back)
    urllib.request.urlretrieve(url, filename)
    points = np.loadtxt(filename)
    return points
