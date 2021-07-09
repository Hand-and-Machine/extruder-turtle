from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

## Set up the turtle
t.name("seven-star.gcode")
t.setup(x=100, y=100)
t.rate(700)

for l in range(30):
    ## Draw a seven-pointed star
    for k in range(7):
        t.forward(50)
        t.right(6*math.pi/7)

    ## Move to the next layer
    t.lift(0.3)

## Save to a GCODE file
t.finish()
