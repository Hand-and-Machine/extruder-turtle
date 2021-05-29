from extruder_turtle import ExtruderTurtle
import math

N = 100
RADIUS = 30
dtheta = 2*math.pi/N
dx = RADIUS*dtheta

t = ExtruderTurtle()

t.name("nonplanar-column.gcode")
t.setup(x=100, y=100)
t.set_density(0.07)
t.rate(500)

for l in range(100):
    prop = l/100
    for k in range(N):
        angle = k*dtheta
        t.move_lift(dx, (1/2)*prop*math.sin(3*angle))
        t.right(dtheta)
    t.lift(0.20)

t.finish()
