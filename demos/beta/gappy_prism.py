from extruder_turtle import ExtruderTurtle
import math
import random

SIDELENGTH = 25
GAPLENGTH = 1
NUM_SIDES = 5
LAYERS = 100

t = ExtruderTurtle()

## Set up the turtle
t.name("gappy-prism.gcode")
t.setup(x=100, y=100)
t.rate(700)

for l in range(LAYERS):
    ## Draw a pentagon
    for k in range(NUM_SIDES):
        ## Draw one side, with a randomly chosen gap
        x = (SIDELENGTH-GAPLENGTH) * random.random()
        t.move(x)
        ## Move out of the way in order to break the plastic strand
        t.penup()
        t.right(math.pi/2)
        t.move(SIDELENGTH)
        t.dwell(50)
        t.left(math.pi)
        t.move(SIDELENGTH)
        t.right(math.pi/2)
        ## Skip over the gap and continue drawing the side
        t.move(GAPLENGTH)
        t.pendown()
        t.move(SIDELENGTH-GAPLENGTH-x)
        t.right(2*math.pi/NUM_SIDES)

    ## Move to the next layer
    t.lift(0.3)

## Save to a GCODE file
t.finish()
