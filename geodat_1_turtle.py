import turtle
import math

dx = 0.01
zoom = 200

t=0
while t<2*3.1415:
	turtle.left(180/3.1415 * dx * 2/math.sqrt(3*math.sin(t)**2 +1)**3)
	turtle.forward(zoom * dx)
	dt = dx / math.sqrt(3*math.sin(t)**2+1)
	t += dt