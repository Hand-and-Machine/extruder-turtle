from extruder_turtle import ExtruderTurtle
import math

## Parameters for the spiral
N = 100                 ## Number of subdivisions of one round-trip
radius = 20             ## Outer radius of the spiral
dtheta = 2*math.pi/N    ## Change in heading after each step
dx = radius * dtheta    ## Forward movement during each step
dr = -radius/N             ## Change in radius with each step

t = ExtruderTurtle()

## Set up the turtle
t.name("evolving-spiral.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(700)

## Continue until the radius has shrunken to zero
for l in range(100):
    prog = l/100
    steps = math.floor(N*(1+2*prog))
    dr = -prog*radius/steps
    for i in range(steps):
        t.move(dx)
        t.right(dtheta)
        radius += dr
        dx = radius * dtheta
    t.lift(0.15)
    for i in range(steps):
        dx = radius * dtheta
        radius += -dr
        t.left(dtheta)
        t.move(-dx)
    t.lift(0.15)

## Save to a GCODE file
t.finish()
