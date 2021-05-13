from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("euler-spiral.gcode")
t.setup(x=100, y=100)
t.rate(700)

N = 500
theta = 2*math.pi/N
for l in range(30):
    for k in range(-N, N+1):
        t.move(1)
        t.right(2*math.pi*k/N)
    t.right(math.pi)
    t.lift(0.3)

t.finish()
