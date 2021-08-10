from extruder_turtle import ExtruderTurtle
import math

## Parameters for the spiral
N = 40                 ## Number of subdivisions of one round-trip
RADIUS = 5             ## Outer radius of the spiral
dtheta = 2*math.pi/N    ## Change in heading after each step
dx = RADIUS * dtheta    ## Forward movement during each step
dr = -0.5/N             ## Change in radius with each step

t = ExtruderTurtle()

t.name("hair-pillar.gcode")
t.setup(x=150, y=150)
t.set_density(0.07) # 0.05
t.rate(500)

radius = RADIUS
while radius>0:
    t.forward(dx)
    t.right(dtheta)
    radius += dr
    dx = radius * dtheta

for l in range(200):
    t.extrude(0.1)
    t.dwell(200)
    t.lift(0.1) # 0.1

t.penup()
t.forward(80)
t.right(math.pi/2)
t.forward(80)
t.right(math.pi)
t.lift(-20)
t.pendown()

radius = RADIUS
dx = RADIUS * dtheta
while radius>0:
    t.forward(dx)
    t.right(dtheta)
    radius += dr
    dx = radius * dtheta

t.penup()
for l in range(200):
    t.extrude(0.2)
    t.dwell(200)
    t.lift(0.1)
    t.rate(5000)
    for i in range(4):
        t.forward(150)
        t.left(math.pi/2)
    t.rate(500)

## Save to a GCODE file
t.finish()
