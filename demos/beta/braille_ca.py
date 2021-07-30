from extruder_turtle import ExtruderTurtle
import math
import random

BUMPLENGTH = 1 ## 2
BUMP_ANGLE = math.pi/3
BUMP_DENSITY = 0.16 ## 0.08
EXT_DENSITY = 0.05      # 0.05
FEEDRATE = 900
LAYER_HEIGHT = 0.3

DIAMETER = 40
NUM_SIDES = 50
LAYERS = 100
dtheta = 2*math.pi/NUM_SIDES
dx = DIAMETER*math.sin(dtheta/2)

t = ExtruderTurtle()

## Set up the turtle
t.name("braille-ca.gcode")
t.setup(x=100, y=100)
t.rate(FEEDRATE)
t.set_density(EXT_DENSITY)

ca = [0]*NUM_SIDES
ca[0] = 1
on_states = [1,2,3,4] # Wolfram's "Rule 30"

for l in range(LAYERS):
    for k in range(NUM_SIDES):
        t.right(dtheta)
        t.forward(dx)
        if ca[k] == 1:
            t.left(BUMP_ANGLE)
            t.forward(BUMPLENGTH)
            t.forward(-BUMPLENGTH)
            t.right(BUMP_ANGLE)
        t.lift(LAYER_HEIGHT/NUM_SIDES)

    ## Update cellular automaton
    if l % 3 == 2:
        new_ca = [0]*NUM_SIDES
        for i in range(NUM_SIDES):
            state_num = ca[(i-1)%NUM_SIDES]*4 + ca[i]*2 + ca[(i+1)%NUM_SIDES]
            if state_num in on_states: new_ca[i] = 1
        ca = new_ca

## Save to a GCODE file
t.finish()
