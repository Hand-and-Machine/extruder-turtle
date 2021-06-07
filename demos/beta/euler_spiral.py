from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("euler-spiral.gcode")
t.setup(x=100, y=100)
t.rate(700)
t.set_density(0.5)

length = 0
dl = 5

for i in range(200):
    length += dl
    t.move(dl)
    t.right(2*math.pi*length*dl/10)
    dl = 5/length

t.finish()
