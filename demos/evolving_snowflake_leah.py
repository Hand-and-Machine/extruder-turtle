from extruder_turtle import ExtruderTurtle
import math

instruction = "frrfrrfrr"
rules = {
            "f": "flfrrflf",
            "r": "r",
            "l": "l"
            }

NUMBER_GENERATIONS = 4
sidelength = 50

t = ExtruderTurtle()

t.name("evolving_snowflake.gcode")
t.setup(x=100, y=100)
t.rate(700)

angle = 60

for g in range(NUMBER_GENERATIONS):
    for l in range(40):
        progress = l/40
        gap_length = progress*sidelength/3
        long_length = (sidelength - gap_length)/2
        for r in instr:
            if r == "f":
                t.forward(long_length)
                t.left(60)
                t.forward(gap_length)
                t.right(2*60)
                t.forward(gap_length)
                t.left(60)
                t.forward(long_length)
            elif r == "r":
                t.right(60)
            elif r == "l":
                t.left(60)
        t.lift(0.3)
    new_instr = ""
    for r in instr:
        new_instr += sub_rules[r]
    instr = new_instr
    sidelength = sidelength/3

t.finish()

word  = "f"
rules = {
          "f": "flfrrflf",
          "r": "r",
          "l": "l"
        }


