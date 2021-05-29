from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

## Set up the turtle
t.name("feedrate-test.gcode")
t.setup(x=100, y=100)

## Parameters
min_rate = 200
max_rate = 10000
height = 200

for l in range(height):
    ## Feedrate increases linearly from one layer to the next,
    ## making the extruder move faster and faster
    t.rate(min_rate + l*(max_rate-min_rate)/height)

    ## Draw a square
    for k in range(4):
        t.move(30)
        t.right(math.pi/2)

    ## Move to the next layer
    t.lift(0.3)

## Save to a GCODE file
t.finish()
