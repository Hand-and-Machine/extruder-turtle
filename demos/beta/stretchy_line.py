from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("stretchy-line.gcode")
t.setup(x=100, y=100)
t.rate(900)
t.set_density(0.05)

for l in range(10):
    t.forward(20)
    t.right(math.pi/2)
    t.forward(5)
    t.left(math.pi/2)
    t.forward(2)
    t.left(math.pi/2)
    t.forward(10)
    t.right(math.pi/2)
    t.forward(2)
    t.right(math.pi/2)
    t.forward(5)
    t.left(math.pi/2)
    t.forward(20)
    t.right(math.pi)
    t.lift(0.3)

t.finish()
