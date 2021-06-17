from extruder_turtle import ExtruderTurtle
import math

HAIR_SPACE = 1
HAIR_ROWS = 10
HAIR_COLS = 10

t = ExtruderTurtle()

t.name("hair-patch.gcode")
t.setup(x=100, y=100)
t.rate(700)

t.set_density(0.05)
## Draw the base
for l in range(3):
    length = (HAIR_COLS+1)*HAIR_SPACE
    width = (HAIR_ROWS+1)*HAIR_SPACE
    while width > 0:
        t.left(math.pi/2)
        t.forward(width)
        t.left(math.pi/2)
        t.forward(length)
        length += -0.5
        width += -0.5
    t.lift(0.25)
    while width < (HAIR_ROWS+1)*HAIR_SPACE:
        width += 0.5
        length += 0.5
        t.backward(length)
        t.right(math.pi/2)
        t.backward(length)
        t.right(math.pi/2)
    t.lift(0.25)

t.finish()
