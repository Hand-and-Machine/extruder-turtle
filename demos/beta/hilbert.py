from extruder_turtle import ExtruderTurtle
import math

instr = "A"
sub_rules = {
    "A": "+BF-AFA-FB+",
    "B": "-AF+BFB+FA-",
    "F": "F",
    "+": "+",
    "-": "-"
}

GENS = 5
sidelength = 50/2**GENS

t = ExtruderTurtle()

t.name("hilbert.gcode")
t.setup(x=100, y=100)
t.set_density(0.05)
t.rate(800)

for g in range(GENS):
    new_instr = ""
    for r in instr:
        new_instr += sub_rules[r]
    instr = new_instr

for l in range(10):
    for r in instr:
        if r == "F": t.forward(sidelength)
        elif r == "+": t.right(math.pi/2)
        elif r == "-": t.left(math.pi/2)
    t.lift(0.3)
    for r in reversed(instr):
        if r == "F": t.backward(sidelength)
        elif r == "+": t.left(math.pi/2)
        elif r == "-": t.right(math.pi/2)
    t.lift(0.3)
    

t.finish()
