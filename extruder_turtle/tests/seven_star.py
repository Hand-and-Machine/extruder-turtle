from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("seven-star.gcode")
t.setup(x=100, y=100)

for l in range(50):
    for k in range(7):
        t.move(20)
        t.right(6*math.pi/7)
    t.lift(0.3)

t.finish()
