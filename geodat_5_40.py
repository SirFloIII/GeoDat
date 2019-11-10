import geodat
from scipy.spatial import KDTree
import numpy as np


import time

eps = 1

# if you change points after constructing the tree, results will be bollocks
points = geodat.getPoints("punktwolke1.txt")

q = points[123]

t0 = time.time()

tree = KDTree(points)

t1 = time.time()

neighbours = points[tree.query_ball_point(q, eps)]

t2 = time.time()

neighbours2 = points[np.linalg.norm(points - q, axis = 1) < eps]

t3 = time.time()

neighbours3 = [p for p in points if (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2 < eps**2]

t4 = time.time()

assert(len(neighbours) == len(neighbours2))
assert(len(neighbours) == len(neighbours3))

print(f"""
Building Tree        : {t1-t0:.4f}s
Searching with Tree  : {t2-t1:.4f}s
Searching with numpy : {t3-t2:.4f}s
Searching naivly     : {t4-t3:.4f}s

Fazit:
    Rosen sind rot
    Veilchen sind blau
    Ich kann nicht reimen
    und C ist schnell
""")
