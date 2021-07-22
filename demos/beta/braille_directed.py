from extruder_turtle import ExtruderTurtle
import math
import random

HAIRLENGTH = 3 ## 2
HAIR_ANGLE = math.pi/6
HAIR_DENSITY = 0.16 ## 0.08
EXT_DENSITY = 0.06      # 0.05
FEEDRATE = 900
LAYER_HEIGHT = 0.3

DIAMETER = 40
NUM_SIDES = 50
LAYERS = 50
dtheta = 2*math.pi/NUM_SIDES
dx = DIAMETER*math.sin(dtheta/2)

t = ExtruderTurtle()

## Set up the turtle
t.name("braille-directed.gcode")
t.setup(x=100, y=100)
t.rate(FEEDRATE)
t.set_density(EXT_DENSITY)

for l in range(LAYERS):
    for k in range(NUM_SIDES):
        t.right(dtheta)
        t.forward(dx)
        if random.random() < HAIR_DENSITY:
            t.penup()
            t.left(HAIR_ANGLE)
            t.forward(HAIRLENGTH)
            t.forward(-HAIRLENGTH)
            t.right(HAIR_ANGLE)
            t.pendown()

    ## Move to the next layer
    t.lift(LAYER_HEIGHT)

## Save to a GCODE file
t.finish()
