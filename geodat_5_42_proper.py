import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import geodat

p = geodat.getPoints("points.txt")
n = geodat.getPoints("normals.txt")

num = len(p)

n_bar = np.cross(p,n)
n_combined = np.concatenate((n, n_bar), axis = 1)
N = np.stack((np.sum(n_combined**2, axis = 1), *n_combined.T, np.ones(num))).T #vandermonde?
constraint_matrix = np.diag([1,1,1,0,0,0])

c_combined = geodat.constrainedWeightedRegression(n_combined, constraint_matrix)

c = c_combined[..., :3]
c_bar = c_combined[..., 3:]

print(f"c      = {c}")
print(f"c_bar  = {c_bar}")

# (c cbar)^t Q (= sum (n nbar)^t (n nbar)) (c cbar) via minSquares
# <c,c_bar>/<c,c> = p
# (g, gbar) = (c, cbar - p c), dh richtungsvektor = g = c
# x = g times gbar /<g,g> 

ell = c.dot(c_bar)/c.dot(c) # schiebanteil
g_bar = c_bar - p*c # https://www.youtube.com/watch?v=ulPgWVC08KI
g = c # uhh... richtungsvektor der achse
x = np.cross(g,g_bar)/g.dot(g) # punkt auf der achse

print(f"lambda = {ell}")
print(f"g      = {g}")
#print(f"g_bar  = {g_bar}")
#print(f"x      = {x}")

'''
We can therefore rewrite Equ. (3.24) in the form(c,c)^T·K·(c,c)→min,
(c,c)^T·D·(c,c) = 1 with two (6×6)-matrices K and D. The matrix D has
nonzero entries only in its upper left 3×3 corner. The solution of
this problem is therefore a general eigenvalueproblem with a cubic
characteristic equation det(K−λD) = 0 (Skript S. 54)
'''

# 43
# rotate g (and points) into 0 0 1

def rot_mat(a,b):
    '''https://math.stackexchange.com/questions/180418/calculate-rotation-matrix-to-align-vector-a-to-vector-b-in-3d/897677#897677'''
    
    v = np.cross(a,b)
    c = np.dot(a,b)

    v_x = np.array([[0, -v[2], v[1]],
                    [v[2], 0, -v[0]],
                    [-v[1], v[0], 0]])

    R = np.identity(3)+v_x + np.dot(v_x,v_x)*1/(1+c)
    return R

R = rot_mat(g,[0,0,1])

p_rot = np.array([np.dot(R,point) for point in p])

# 2) rotate the points into the yz plane

phi = np.arctan2(p_rot[:,0], p_rot[:,1])

c = np.cos(phi)
s = np.sin(phi)

z = np.zeros(num)
o = np.ones(num)

A = np.array(([ c, s, z],
              [-s, c, z],
              [ z, z, o])).T
              
q = np.array([a@s for a,s in zip(A, p_rot)])

# min square polynom interpolieren (nicht notwendig)

def ausgleichsPolynom(points, deg):
    X = np.array(list(map(lambda p: [p[0]**i for i in range(deg+1)], points)))
    Xt = np.linalg.pinv(X)
    b = z[:,1]
    a = Xt.dot(b)
    return a

# rotate it all back (nicht notwendig)

# plot the whole mess

# plot in 3d

fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')

ax.set_zlim(-4, 4)

ax.scatter(*p.T, s=1, c = (n+1)/2)

# von "oben"

ax = fig.add_subplot(222)
ax.axis("equal")

ax.scatter(p[:,0], p[:, 1], s = 1, c = (n+1)/2)

# in fläche rotiert

ax = fig.add_subplot(223)
ax.axis("equal")

ax.scatter(q[:,1], q[:, 2], s = 1, c = phi)

# schraubanteil abgezogen

ax = fig.add_subplot(224)
ax.axis("equal")

ax.scatter(q[:,1], q[:, 2] - ell*phi, s = 1, c = phi)

plt.show()

####################
#                  #
# WISHFUL THINKING #
#                  #
####################

print("WISHFUL THINKING")

# plot in 3d
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')

ax.set_zlim(-4, 4)

ax.scatter(*p.T, s=1, c = (n+1)/2)

# von "oben"
ax = fig.add_subplot(222)
ax.axis("equal")

ax.scatter(p[:,0], p[:, 1], s = 1, c = (n+1)/2)

# postuliere: drehachse ist z achse durch den nullpunkt
# drehe punkte in die x-z achse und färbe nach drehwinkel ein:

ax = fig.add_subplot(223)
ax.axis("equal")

phi = np.arctan2(p[:,0], p[:,1])

c = np.cos(phi)
s = np.sin(phi)

z = np.zeros(num)
o = np.ones(num)

A = np.array(([ c, s, z],
              [-s, c, z],
              [ z, z, o])).T
              
q = np.array([a@s for a,s in zip(A, p)])
ax.scatter(q[:,1], q[:, 2], s = 1, c = phi)

# errate schraubanteil:

ax = fig.add_subplot(224)
ax.axis("equal")

c = -0.5

ax.scatter(q[:,1], q[:, 2] - c*phi, s = 1, c = phi)

plt.show()
