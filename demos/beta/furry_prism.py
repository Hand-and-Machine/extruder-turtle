from extruder_turtle import ExtruderTurtle
import math
import random

HAIRLENGTH = 1
HAIR_ANGLE = math.pi/3
EXT_DENSITY = 0.05
FEEDRATE = 500
NUM_HAIRS = 15
LAYER_HEIGHT = 0.15

SIDELENGTH = 25
NUM_SIDES = 5
LAYERS = 100
dx = SIDELENGTH/(NUM_HAIRS+1)

t = ExtruderTurtle()

## Set up the turtle
t.name("furry-prism.gcode")
t.setup(x=100, y=100)
t.rate(FEEDRATE)
t.set_density(EXT_DENSITY)

for l in range(LAYERS):
    ## Draw a pentagon
    for k in range(NUM_SIDES):
        t.move(dx)
        for n in range(NUM_HAIRS):
            t.left(HAIR_ANGLE)
            t.move(HAIRLENGTH)
            t.move(-HAIRLENGTH)
            t.right(HAIR_ANGLE)
            t.move(dx)
        t.right(2*math.pi/NUM_SIDES)

    ## Move to the next layer
    t.lift(LAYER_HEIGHT)

## Save to a GCODE file
t.finish()
