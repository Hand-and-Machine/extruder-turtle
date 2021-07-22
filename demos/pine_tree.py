from extruder_turtle import ExtruderTurtle
import math

## Parameters for the spiral base
N = 40                 ## Number of subdivisions of one round-trip
radius = 20             ## Outer radius of the spiral
dtheta = 2*math.pi/N    ## Change in heading after each step
dx = radius * dtheta    ## Forward movement during each step
dr = -0.5/N             ## Change in radius with each step

t = ExtruderTurtle()

## Set up the turtle
t.name("pine-tree.gcode")
t.setup(x=100, y=100)
t.set_density(0.07) # 0.05
t.rate(500)

# Draw the spiral base
while radius>0:
    t.forward(dx)
    t.right(dtheta)
    radius += dr
    dx = radius * dtheta

## Bottom of the trunk
for l in range(50):
    t.extrude(0.1)
    t.dwell(100)
    t.lift(0.05) # 0.1

## Upper part of the trunk, with needles
for x in range(60):
    for l in range(10):
        t.extrude(0.1)
        t.dwell(100)
        t.lift(0.1)
    for n in range(5):
        t.forward(10-x/6)
        t.left(math.pi/6)
        t.forward(10-x/6)
        t.left(5*math.pi/6)
        t.forward(10-x/6)
        t.left(math.pi/6)
        t.forward(10-x/6)
        t.left(math.pi/6)
        t.left(math.pi/5)
    t.left(math.pi/7)

## Save to a GCODE file
t.finish()
