from extruder_turtle import ExtruderTurtle
import math
import random

N = 100
DIAMETER = 50
dtheta = 2*math.pi/N
dx = DIAMETER*math.sin(dtheta/2)

t = ExtruderTurtle()

## Set up the turtle
t.name("dreamcatcher.gcode")
t.setup(x=100, y=100)
t.rate(700)

for l in range(50):
    ## Draw a circle
    t.set_density(0.07)
    t.left(dtheta/2)
    for k in range(N):
        t.right(dtheta)
        t.forward(dx)
    t.right(dtheta/2)

    ## Draw a random chord on the circle
    t.dwell(100)
    t.set_density(0.03)    
    rand_angle = dtheta*random.randint(1,N)/2
    t.right(rand_angle)
    t.forward(DIAMETER*math.sin(rand_angle))
    t.right(rand_angle)

    ## Move to the next layer
    t.lift(0.3)

## Save to a GCODE file
t.finish()
