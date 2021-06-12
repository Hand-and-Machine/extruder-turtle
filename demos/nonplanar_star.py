from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

## Set up turtle
t.name("nonplanar-star.gcode")
t.setup(x=100, y=100)
t.rate(500)

for l in range(30):
    ## Track progress
    vert_prop = l/30

    ## Draw a seven-pointed star
    for k in range(7):
        ## Each line is slightly parabolically curved
        ## The bottom layer is completely flat, but
        ## subsequent layers are increasingly curved
        for x in range(-25, 26):
            horiz_prop = x/25
            t.forward_lift(1, -vert_prop*horiz_prop*0.3)
        t.right(6*math.pi/7)

    ## Move to the next layer
    t.lift(0.15)

## Save to a GCODE file
t.finish()
