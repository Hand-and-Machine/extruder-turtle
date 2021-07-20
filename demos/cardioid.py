from extruder_turtle import ExtruderTurtle
import math
import random

N = 67          ## For best results, this should be a modulus for which
                ## 2 is a primitive root modulo N
DIAMETER = 50
dtheta = 2*math.pi/N
dx = DIAMETER*math.sin(dtheta/2)
n = 1

t = ExtruderTurtle()

## Set up the turtle
t.name("cardioid.gcode")
t.setup(x=100, y=100)
t.rate(700)

for l in range(N-1):
    ## Draw a circle
    t.set_density(0.07)
    t.left(dtheta/2)
    for k in range(N):
        t.right(dtheta)
        t.forward(dx)
    t.right(dtheta/2)
    
    ## Draw several chords
    for i in range(8):
        t.dwell(100)
        t.set_density(0.03)
        angle = n*dtheta/2
        t.right(angle)
        t.forward(DIAMETER*math.sin(angle))
        t.right(angle)
        ## Point n is joined by a line segment to point 2n
        n = (2*n) % N

    ## Move to the next layer
    t.lift(0.3)

## Save to a GCODE file
t.finish() 
