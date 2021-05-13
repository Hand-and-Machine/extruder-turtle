from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("nonplanar-column.gcode")
t.setup(x=100, y=100)
t.set_density(0.07)
t.rate(500)

N = 100
radius = 30
dtheta = 2*math.pi/N
dx = radius*dtheta
for l in range(100):
    prop = l/100
    for k in range(N):
        angle = k*dtheta
        t.move_lift(dx, prop*math.sin(2*angle))
        t.right(dtheta)
    t.lift(0.15)

t.finish()
