from extruder_turtle import ExtruderTurtle
import math

N = 100
radius = 30
dtheta = 2*math.pi/N
dx = radius * dtheta
dr = -0.5/N

t = ExtruderTurtle()

t.name("spiral.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(700)

while radius>0:
    t.move(dx)
    t.right(dtheta)
    radius += dr
    dx = radius * dtheta

t.finish()
