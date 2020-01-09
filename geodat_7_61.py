# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 17:04:08 2020

@author: Flo
"""

import numpy as np
import itertools
import collections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # noqa


def angle_between_points(a,b,c):
    ba = a - b
    bc = c - b
    
    cosine_of_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    
    return np.arccos(cosine_of_angle)

class Dreiecksnetz:
    
    def __init__(self, vertices, pos_func, neighbor_func):
        
        self.vertices = set()
        self.positions = dict()
        self.edges = set()
        self.neighbors = collections.defaultdict(set)
        self.tris = set()
        self.tri_neighbors = collections.defaultdict(set)
        
        self.add_vertices(vertices)
        self.set_positions_parametric(pos_func)
        self.set_edges_parametric(neighbor_func)
        self.find_tris()
        
        
    def add_vertices(self, idx):
        
        for i in idx:
            self.vertices.add(i)
    
    def set_positions_parametric(self, pos_func):
        
        for i in self.vertices:
            self.positions[i] = pos_func(i)
            
    def set_edges_parametric(self, neighbor_func):
        
        for v in self.vertices:
            for w in neighbor_func(v):
                if w in self.vertices:
                    self.edges.add((v, w))
                    self.edges.add((w, v))
                    self.neighbors[v].add(w)
                    self.neighbors[w].add(v)
                    
    def find_tris(self):
        
        for v in self.vertices:
            for x, y in itertools.product(self.neighbors[v], repeat = 2):
                if (x, y) in self.edges:
                    self.tris.add((v,x,y))
                    self.tri_neighbors[v].add((x,y))
                    
#    def inner_check(self, v):
#        assert v in self.vertices
#        
#        if len(self.tri_neighbors(v)) == 0:
#            return False
#        else:
#            # TODO
        
    
    def H(self, v):
        assert v in self.vertices
        
        return 1/2 * sum([1/np.tan(angle_between_points(self.positions[v],
                                                        self.positions[u],
                                                        self.positions[w])
        ) * (self.positions[w] - self.positions[v]) for w, u in self.tri_neighbors[v]])
    
    
    
if __name__ == "__main__":
    
    case = 3
    
    if case == 1:
        
        n = 10
        m = 20
    
        def pos(idx):
            i, j = idx
            return np.array((i, j, 0))
    
    elif case == 2:
        
        m = 21
        n = m
        
        M = (m-1)//2
        N = (n-1)//2
        
        def pos(idx):
            i, j = idx
            
            x = (i-1)/M - 1
            y = (j-1)/N - 1
            
            return np.array((x,
                             y,
                             np.sqrt(2 - x**2 - y**2)))
    
    elif case == 3:
        
        m = 20
        n = m
        
        def pos(idx):
            i, j = idx
            
            u = -2 + (i - 1) * 4 / (m - 1)
            v = (j - 1) * 2 * np.pi / (n - 1)
            
            return np.array((np.cos(v)*np.cosh(u),
                             np.sin(v)*np.cosh(u),
                             u))
    
    else:
        assert case in [1,2,3]
    
    def neighbor_func(idx):
        i,j = idx
        return [(i + 1, j    ),
                (i + 1, j + 1),
                (i    , j + 1)]

    netz = Dreiecksnetz(itertools.product(range(1,m+1), range(1,n+1)), pos, neighbor_func)
    
    p = []
    k = []
    for v in netz.vertices:
        if v[0] != 1 and v[1] != 1 and v[0] != m and v[1] != n: #if inner pointß
            p.append(netz.positions[v])
            k.append(netz.H(v))
    
    p = np.array(p).T
    k = np.array(k).T
    
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(*p, s = 2)
    ax.quiver(*p, *k, length = 5)
    
    
    plt.axis("equal")    
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    