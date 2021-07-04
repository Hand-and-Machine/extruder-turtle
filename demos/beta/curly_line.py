from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("curly-line.gcode")
t.setup(x=100, y=100)
t.rate(700)

t.set_density(0.2)

t.lift(1)
t.forward(100)
t.left(math.pi/2)
t.penup()
t.lift(10)
t.forward(20)
t.lift(-10)
t.left(math.pi/2)
t.lift(1)
t.pendown()
t.forward(100)
t.right(math.pi/2)
t.penup()
t.lift(10)
t.forward(20)
t.lift(-10)
t.right(math.pi/2)
t.lift(1)
t.pendown()
t.forward(100)

t.finish()
