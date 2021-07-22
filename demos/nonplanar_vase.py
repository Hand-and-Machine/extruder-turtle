from extruder_turtle import ExtruderTurtle
import math

## Parameters for vase and rim oscillations
N = 100
RADIUS = 20
PERIODS = 3
AMPLITUDE = 6
LAYERS = 200
dtheta = 2*math.pi/N
dx = RADIUS*dtheta
radius = RADIUS

t = ExtruderTurtle()

## Set up the turtle
t.name("nonplanar-vase.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(500)

## Draw a spiral base
dr = 0.5/60
base_rad = 0
base_dx = 0
while base_rad < RADIUS:
    t.forward(base_dx)
    t.right(2*math.pi/60)
    base_rad += dr
    base_dx = base_rad * 2*math.pi/60

## First few layers "bulding up" the oscillations
for l in range(20):
    prop = l/20
    total_prop = l/LAYERS
    for k in range(N):
        angle = k*dtheta
        t.forward_lift(dx, PERIODS*AMPLITUDE*prop*math.sin(PERIODS*angle)/N)
        t.right(dtheta)
        t.lift(0.25/N)
    t.left(math.pi/2)
    radius_delta = RADIUS*math.sin(1.5*math.pi*(total_prop+1/3))/(LAYERS/2)
    t.forward(radius_delta)
    radius += radius_delta
    dx = radius*dtheta
    t.right(math.pi/2)

## The rest of the layers, with full oscillations
for l in range(LAYERS-20):
    total_prop = (l+20)/LAYERS
    for k in range(N):
        angle = k*dtheta
        t.forward_lift(dx, PERIODS*AMPLITUDE*math.sin(PERIODS*angle)/N)
        t.right(dtheta)
        t.lift(0.25/N)
    t.left(math.pi/2)
    radius_delta = RADIUS*math.sin(1.5*math.pi*(total_prop+1/3))/(LAYERS/2)
    t.forward(radius_delta)
    radius += radius_delta
    dx = radius*dtheta
    t.right(math.pi/2)

## Save the GCODE file
t.finish()
