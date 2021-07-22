from extruder_turtle import ExtruderTurtle
import math

## L-system for the Koch Snowflake
instr = "frrfrrfrr"
sub_rules = {
            "f": "flfrrflf",
            "r": "r",
            "l": "l"
            }

GENS = 5
sidelength = 50/3**GENS

for g in range(GENS):
    new_instr = ""
    for r in instr:
        new_instr += sub_rules[r]
    instr = new_instr

t = ExtruderTurtle()

t.name("snowflake-lsystem.gcode")
t.setup(x=100, y=100)
t.rate(700)

for l in range(40):
    for r in instr:
        if r == "f": t.forward(sidelength)
        elif r == "r": t.right(math.pi/3)
        elif r == "l": t.left(math.pi/3)
    t.lift(0.3)

t.finish()
