import numpy as np

zoomx = 12
zoomy = 6
sizex = zoomx*4+4
sizey = zoomy*4+4

a = np.array([["." for j in range(sizex)] for i in range(sizey)])

def xytoij(x,y):
	i = int(sizey/2 - zoomy*y)
	j = int(sizex/2 + zoomx*x)
	return i, j

def ijtoxy(i,j):
	x = (j-sizex/2)/zoomx
	y = -(i-sizey/2)/zoomy
	return x, y
	
midi, midj = xytoij(0,0)

a[midi, :] = "-"
a[:, midj] = "|"
a[midi, midj] = "+"

bx = 2
by = 1

epsx = 1/zoomx/2
epsy = 1/zoomy/2

for i in range(sizey):
	for j in range(sizex):
		x, y = ijtoxy(i,j)
		if (x/(bx-epsx))**2 + (y/(by-epsy))**2 > 1 and (x/(bx+epsx))**2 + (y/(by+epsy))**2 < 1:
			a[i,j] = "#"
			
"""
t = np.linspace(0, 2*np.pi, num = 200)
x = 2 * np.cos(t)
y = np.sin(t)

for u,v in zip(x,y):
	i, j = xytoij(u,v)
	a[i,j] = "#"
"""


for i in range(sizey):
	print(*a[i], sep="")
