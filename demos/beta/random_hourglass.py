from extruder_turtle import ExtruderTurtle
import math
import random

t = ExtruderTurtle()

t.name("random-hourglass.gcode")
t.setup(x=100, y=100)
t.rate(500)
t.set_density(0.04)

for l in range(240*7):
    t.forward(10*math.sqrt(12*(l/(240*7)-1/2)**2 + 1))
    t.right(2*math.pi/7 + math.pi*random.random()/500)
    t.lift(0.2/7)
    t.lift(1)
    t.extrude(0.4)
    t.lift(-1)
    t.dwell(200)

t.finish()
