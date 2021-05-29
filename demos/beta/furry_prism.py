from extruder_turtle import ExtruderTurtle
import math
import random

SIDELENGTH = 25
HAIRLENGTH = 1
HAIR_ANGLE = math.pi/3
NUM_HAIRS = 15
NUM_SIDES = 5
LAYERS = 150
dx = SIDELENGTH/(NUM_HAIRS+1)

t = ExtruderTurtle()

## Set up the turtle
t.name("furry-prism.gcode")
t.setup(x=100, y=100)
t.rate(700)

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
    t.lift(0.3)

## Save to a GCODE file
t.finish()
