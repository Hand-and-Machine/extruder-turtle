from extruder_turtle import ExtruderTurtle
import math
import random

HAIRLENGTH = 1
HAIR_ANGLE = math.pi/2
EXT_DENSITY = 0.01      # 0.02
FEEDRATE = 700
NUM_HAIRS = 200
LAYER_HEIGHT = 0.3

DIAMETER = 80
NUM_SIDES = 5
LAYERS = 200
dtheta = 2*math.pi/NUM_HAIRS
dx = DIAMETER*math.sin(dtheta/2)

t = ExtruderTurtle()

## Set up the turtle
t.name("flex-circle.gcode")
t.setup(x=100, y=100)
t.rate(FEEDRATE)
t.set_density(EXT_DENSITY)

for l in range(LAYERS):
    for k in range(NUM_HAIRS):
        t.right(dtheta)
        t.forward(dx)
        t.left(HAIR_ANGLE)
        t.forward(HAIRLENGTH)
        t.dwell(50)
        t.forward(-2*HAIRLENGTH)
        t.dwell(50)
        t.forward(HAIRLENGTH)
        t.right(HAIR_ANGLE)

    ## Move to the next layer
    t.lift(LAYER_HEIGHT)

## Save to a GCODE file
t.finish()
