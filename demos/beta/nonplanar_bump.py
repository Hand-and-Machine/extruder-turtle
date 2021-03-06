from extruder_turtle import ExtruderTurtle
import math

N = 30
RADIUS = 20
dtheta = 2*math.pi/N
dx = RADIUS*dtheta
dr = -0.5/N
MAX_HEIGHT = 6

t = ExtruderTurtle()

t.name("nonplanar-bump.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(1000)

for l in range(10):
    radius = RADIUS
    prop = l/10
    while radius > 0:
        t.move_lift(dx, prop*radius*2*MAX_HEIGHT/(-RADIUS**2/dr - RADIUS))
        t.right(dtheta)
        radius += dr
        dx = radius * dtheta
    t.lift(0.15)
    while radius < RADIUS:
        radius += -dr
        dx = radius * dtheta
        t.left(dtheta)
        t.move_lift(-dx, -prop*radius*2*MAX_HEIGHT/(-RADIUS**2/dr - RADIUS))
    t.lift(0.15)

t.finish()
