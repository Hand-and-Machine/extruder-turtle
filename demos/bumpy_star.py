from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

## Set up the turtle
t.name("bumpy-star.gcode")
t.setup(x=100, y=100)
t.rate(700)

t.set_density(0.3)
t.lift(1)

for l in range(9): # height of 10.5
    ## Draw a seven-pointed star
    for k in range(7):
        t.forward(50)
        t.right(6*math.pi/7)

    ## Move to the next layer
    t.lift(1.2)  # 0.7 for first demo, 0.6 for second demo, 0.9 for third demo, 1.2 for fourth demo 
                 # 0.5 gets too squished
                 # 1 gets too bumpy

## Save to a GCODE file
t.finish()
