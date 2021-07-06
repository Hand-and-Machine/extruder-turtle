from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("complex-walk.gcode")
t.setup(x=100, y=100)
t.rate(700)

N = 75
period = 224
angle = 2*math.pi/N

for l in range(30):
    for k in range(period+1):
        t.forward(2)
        t.right(angle*k*(k-1)/2)
    t.lift(0.3)

t.finish()
