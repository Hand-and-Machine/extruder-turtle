from extruder_turtle import ExtruderTurtle
import math

N = 100
RADIUS = 20
dtheta = 2*math.pi/N
dx = RADIUS*dtheta

t = ExtruderTurtle()

## Set up the turtle
t.name("spirograph.gcode")
t.setup(x=100, y=100)
t.rate(700)

for l in range(50):
    ## Draw the spirograph
    for k in range(N):
        t.move(dx)
        t.right(dtheta*(1 + (1/3)*math.sin(20*math.pi*k/N)))
    
    ## Move to the next layer
    t.lift(0.3)

## Save the GCODE file
t.finish()
