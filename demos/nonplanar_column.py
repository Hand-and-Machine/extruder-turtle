from extruder_turtle import ExtruderTurtle
import math

## Parameters for the cylinder
N = 100
RADIUS = 20
PERIODS = 3
AMPLITUDE = 6
dtheta = 2*math.pi/N
dx = RADIUS*dtheta

t = ExtruderTurtle()

## Set up the turtle
t.name("nonplanar-column.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(900)

## First layers, "building up" the oscillations
for l in range(20):
    prop = l/20
    for k in range(N):
        angle = k*dtheta
        t.forward_lift(dx, PERIODS*AMPLITUDE*prop*math.sin(PERIODS*angle)/N)
        t.right(dtheta)
        t.lift(0.25/N)

## Later layers, with full oscillations
for l in range(80):
    for k in range(N):
        angle = k*dtheta
        t.forward_lift(dx, PERIODS*AMPLITUDE*math.sin(PERIODS*angle)/N)
        t.right(dtheta)
        t.lift(0.25/N)

## Save the GCODE file
t.finish()
