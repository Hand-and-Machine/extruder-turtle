from extruder_turtle import ExtruderTurtle
import math
import random

SIDELENGTH = 20
BUMPLENGTH = 1
BUMP_ANGLE = math.pi/2
NUM_SIDES = 6
LAYERS = 100

t = ExtruderTurtle()

## Set up the turtle
t.name("bumpy-prism.gcode")
t.setup(x=100, y=100)
t.rate(700)
t.set_density(0.07)

for l in range(LAYERS):
    ## Draw a pentagon
    for k in range(NUM_SIDES):
        ## Draw one side, with a randomly placed bump
        x = SIDELENGTH * random.random()
        t.move(x)
        t.left(BUMP_ANGLE)
        t.rate(100)
        t.move(BUMPLENGTH)
        t.dwell(50)
        t.move(-BUMPLENGTH)
        t.rate(700)
        t.right(BUMP_ANGLE)
        t.move(SIDELENGTH-x)
        t.right(2*math.pi/NUM_SIDES)

    ## Move to the next layer
    t.lift(0.3)

## Save to a GCODE file
t.finish()
