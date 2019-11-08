from geodat import *
from scipy.spatial import KDTree

eps = 1

# if you change points after constructing the tree, results will be bollocks
points = getPoints("punktwolke1.txt")
tree = KDTree(points)

neighbours = points[tree.query_ball_point(points[123],eps)]
