from extruder_turtle import ExtruderTurtle
import math
import random

HAIRLENGTH = 1 ## 2
HAIR_ANGLE = math.pi/3
HAIR_DENSITY = 0.16 ## 0.08
EXT_DENSITY = 0.03      # 0.05
FEEDRATE = 900
LAYER_HEIGHT = 0.3

DIAMETER = 40
NUM_SIDES = 50
LAYERS = 50
dtheta = 2*math.pi/NUM_SIDES
dx = DIAMETER*math.sin(dtheta/2)

t = ExtruderTurtle()

## Set up the turtle
t.name("braille-circle.gcode")
t.setup(x=100, y=100)
t.rate(FEEDRATE)
t.set_density(EXT_DENSITY)

for l in range(LAYERS):
    for k in range(NUM_SIDES):
        t.right(dtheta)
        t.forward(dx)
        if random.random() < HAIR_DENSITY:
            t.left(HAIR_ANGLE)
            t.forward(HAIRLENGTH)
            t.forward(-HAIRLENGTH)
            t.right(HAIR_ANGLE)

    ## Move to the next layer
    t.lift(LAYER_HEIGHT)

## Save to a GCODE file
t.finish()
