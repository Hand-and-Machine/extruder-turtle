from extruder_turtle import ExtruderTurtle
import math

LENGTH = 20
PILLAR_ROWS = 8

t = ExtruderTurtle()

## Set up the turtle
t.name("pillar-array.gcode")
t.setup(x=100, y=100)
t.lift(0.1)
t.rate(700)
t.set_density(0.05)

num_zigzags = math.floor(LENGTH/0.4)
for i in range(num_zigzags):
    t.forward(LENGTH)
    t.right(math.pi/2)
    t.forward(0.2)
    t.right(math.pi/2)
    t.forward(LENGTH)
    t.left(math.pi/2)
    t.forward(0.2)
    t.left(math.pi/2)

t.lift(0.1)
pillar_space = LENGTH/PILLAR_ROWS
t.penup()
t.rate(1500)
for i in range(PILLAR_ROWS):
    for j in range(PILLAR_ROWS):
        t.extrude(0.1)
        t.lift(20)
        t.forward(pillar_space)
        t.lift(-20)
    if i%2 == 1:
        t.right(math.pi/2)
        t.forward(pillar_space)
        t.right(math.pi/2)
    else:
        t.left(math.pi/2)
        t.forward(pillar_space)
        t.left(math.pi/2)

t.finish()
