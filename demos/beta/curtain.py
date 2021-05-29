from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("curtain.gcode")
t.setup(x=100, y=100)
t.rate(700)

t.penup()
for l in range(100):
    t.extrude(1)
    t.lift(1)
    t.dwell(50)
    t.move(50)
    t.lift(-1)
    t.extrude(1)
    t.lift(1)
    t.dwell(50)
    t.move(-50)
    t.lift(-0.7)

for s in range(20):
    t.pendown()
    progress = s/20
    t.set_density(1 - progress*0.95)
    t.move(50)
    t.lift(1)
    t.penup()
    t.move(-50)
    t.lift(-0.7)

t.finish()
