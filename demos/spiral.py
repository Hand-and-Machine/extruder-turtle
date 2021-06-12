from extruder_turtle import ExtruderTurtle
import math

## Parameters for the spiral
N = 100                 ## Number of subdivisions of one round-trip
radius = 30             ## Outer radius of the spiral
dtheta = 2*math.pi/N    ## Change in heading after each step
dx = radius * dtheta    ## Forward movement during each step
dr = -0.5/N             ## Change in radius with each step

t = ExtruderTurtle()

## Set up the turtle
t.name("spiral.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(700)

## Continue until the radius has shrunken to zero
while radius>0:
    t.forward(dx)
    t.right(dtheta)
    radius += dr
    dx = radius * dtheta

## Save to a GCODE file
t.finish()
