from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("horizontal-brush.gcode")
t.setup(x=200, y=100)
t.rate(700)
t.set_density(0.05)

for l in range(100):
    t.forward(5)
    t.right(math.pi/2)
    t.forward(20)
    t.right(math.pi/2)
    t.forward(5)
    t.right(math.pi/2)
    if l%5 == 3:
        t.forward(0.5)
        for i in range(19):
            t.left(math.pi/2)
            t.rate(3000)
            t.set_density(0.02)
            t.forward(50)
            t.lift(0.2-l*0.2)
            t.penup()
            t.forward(10)
            t.lift(l*0.2-0.2)
            t.forward(-10)
            t.lift(10)
            t.right(math.pi)
            t.forward(50)
            t.pendown()
            t.rate(700)
            t.set_density(0.05)
            t.left(math.pi/2)
            t.forward(1)
            t.lift(-10)
        t.forward(0.5)
    else:
        t.forward(20)
    t.right(math.pi/2)
    t.lift(0.2)

t.finish()
