from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("hair-pillar.gocde")
t.setup(x=100, y=100)
t.rate(700)
t.set_density(0.05)

for l in range(60):
    t.forward(4)
    t.right(math.pi/2)
    t.forward(8)
    t.right(math.pi/2)
    t.forward(8)
    t.right(math.pi/2)
    t.forward(8)
    t.right(math.pi/2)
    t.forward(4)
    t.left(math.pi/2)
    if l%10 != 9: t.penup()
    t.forward(100)
    t.pendown()
    t.left(math.pi/2)
    t.lift(0.1)

t.finish()
