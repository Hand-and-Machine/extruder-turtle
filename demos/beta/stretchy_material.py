from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("stretchy-material.gcode")
t.setup(x=100, y=100)
t.rate(900)
t.set_density(0.05)

for l in range(5):
    for r in range(5):
        for n in range(4):
            t.forward(10)
            t.right(math.pi/2)
            t.forward(4)
            t.left(math.pi/2)
            t.forward(2)
            t.left(math.pi/2)
            t.forward(8)
            t.right(math.pi/2)
            t.forward(2)
            t.right(math.pi/2)
            t.forward(4)
            t.left(math.pi/2)
        sgn = (-1)**(r%2)
        t.forward(10)
        t.left(math.pi/2*sgn)
        t.forward(14)
        t.left(math.pi/2*sgn)
    t.left(math.pi/2)
    for c in range(5):
        t.forward(70)
        t.right(math.pi/2)
        t.forward(10)
        t.right(math.pi/2)
        t.forward(70)
        t.left(math.pi/2)
        t.forward(4)
        t.left(math.pi/2)
    t.forward(70)
    t.left(math.pi/2)
    t.forward(4)
    t.lift(0.2)

t.finish()
