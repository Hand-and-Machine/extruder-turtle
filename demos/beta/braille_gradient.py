from extruder_turtle import ExtruderTurtle
import math
import random

HAIRLENGTH = 1 ## 2
HAIR_ANGLE = math.pi/3
MIN_HAIR_DENSITY = 0
MAX_HAIR_DENSITY = 0.2
EXT_DENSITY = 0.06      # 0.05
FEEDRATE = 900
LAYER_HEIGHT = 0.3

DIAMETER = 40
NUM_SIDES = 200
LAYERS = 100
dtheta = 2*math.pi/NUM_SIDES
dx = DIAMETER*math.sin(dtheta/2)

t = ExtruderTurtle()

## Set up the turtle
t.name("braille-gradient.gcode")
t.setup(x=100, y=100)
t.rate(FEEDRATE)
t.set_density(EXT_DENSITY)

for l in range(LAYERS):
    prog = l/LAYERS
    hair_density = (1-prog)*MIN_HAIR_DENSITY + prog*MAX_HAIR_DENSITY
    for k in range(NUM_SIDES):
        t.right(dtheta)
        t.forward(dx)
        if random.random() < hair_density:
            t.left(HAIR_ANGLE)
            t.forward(HAIRLENGTH)
            t.forward(-HAIRLENGTH)
            t.right(HAIR_ANGLE)

    ## Move to the next layer
    t.lift(LAYER_HEIGHT)

## Save to a GCODE file
t.finish()
