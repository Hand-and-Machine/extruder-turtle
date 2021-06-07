from extruder_turtle import ExtruderTurtle
import math

N = 60
RADIUS = 12
dtheta = 2*math.pi/N
dx = RADIUS*dtheta
dr = -5/N
MAX_HEIGHT = 10

t = ExtruderTurtle()

t.name("spiral-tower.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(1000)

for l in range(40):
    radius = RADIUS
    prop = l/40
    while radius > 0:
        t.move_lift(dx, prop*MAX_HEIGHT*(-dr)/RADIUS)
        t.right(dtheta)
        radius += dr
        dx = radius * dtheta
    t.lift(0.2)
    while radius < RADIUS:
        radius += -dr
        dx = radius * dtheta
        t.left(dtheta)
        t.move_lift(-dx, prop*MAX_HEIGHT*dr/RADIUS)
    t.lift(0.2)

t.finish()
