from extruder_turtle import ExtruderTurtle
import math

HAIR_SPACE = 2
HAIR_ROWS = 10
LIFT_DIST = 10 
EXTRUDE_AMT = 0.5

t = ExtruderTurtle()

t.name("hair-patch.gcode")
t.setup(x=100, y=100)
t.rate(1000)

t.set_density(0.05)
## Draw the base
for l in range(3):
    length = (HAIR_ROWS+1)*HAIR_SPACE
    while length > 0:
        t.left(math.pi/2)
        t.forward(length)
        t.left(math.pi/2)
        t.forward(length)
        length += -0.7
    t.lift(0.2)
    while length < (HAIR_ROWS+1)*HAIR_SPACE:
        length += 0.7
        t.backward(length)
        t.right(math.pi/2)
        t.backward(length)
        t.right(math.pi/2)
    t.lift(0.2)

t.lift(LIFT_DIST+0.2)
t.set_density(0.01)
t.penup()
hairs = HAIR_ROWS
t.forward(-HAIR_SPACE/2)
t.left(math.pi/2)
t.forward(HAIR_SPACE/2)
while hairs > 0:
    for i in range(2):    
        for r in range(hairs):
            t.forward(HAIR_SPACE)
            t.lift(-LIFT_DIST)
            t.extrude(EXTRUDE_AMT)   # 0.5
            t.penup()
            t.lift(2)
            t.extrude(-0.1)
            t.lift(LIFT_DIST-2)
            ## t.pendown()
            t.dwell(100)    # 100
        t.left(math.pi/2)
    hairs += -1
t.finish()
