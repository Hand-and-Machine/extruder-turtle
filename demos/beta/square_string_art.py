from extruder_turtle import ExtruderTurtle
import math

t = ExtruderTurtle()

t.name("square-string-art.gcode")
t.setup(x=100, y=100)
t.rate(500)

t.set_density(0.06)
for l in range(50):
    x = 5*(l%10)
    y = 5*(l%10)
    theta = math.atan(y/(50-x))
    r = math.sqrt((50-x)**2 + y**2)
    for i in range(3):
        t.forward(50)
        t.left(math.pi/2)
        t.forward(50)
        t.left(math.pi*3/4)
        t.forward(50*math.sqrt(2))
        t.left(math.pi*3/4)
        t.lift(0.3)
    t.lift(-0.2)
    t.set_density(0.03)
    t.forward(x)
    t.left(theta)
    t.forward(r)
    t.forward(-r)
    t.right(theta)
    t.forward(-x)
    t.lift(0.2)
    t.set_density(0.06)
    t.pendown()

t.finish()
