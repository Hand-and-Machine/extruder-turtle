# extruder-turtle

A Python package that uses the principles of Turtle Geometry to generate GCODE for 3d-printed solids.

## Basic functionality

The `ExtruderTurtle` class is very simple, and only has a few built-in functions implementing the basic functionality of a turtle.

### Setup

Here are several methods of the `ExtruderTurtle` class that are used to set up your turtle:

- The constructor `t = ExtruderTurtle()` which takes no arguments. The turtle is constructed with a few default values in place:
    - The default output file name `turtle.gcode`
    - Default starting `heading` (the direction of the turtle) is `0`.
    - Default starting `feedrate` (the rate of movement) is `0`.
    - Default starting `density` (ratio of mm extruded to mm moved) is `0`.
    - Default starting `pendown` value (whether or not the turtle extrudes while moving) is `True`
- To change the name of the output file, use `t.name("your-filename.gcode")`
- To write the initialization sequence (which moves the turtle to the initial position, runs the mesh bed leveling, heats the bed and extruder, etc) to the output file, run `t.setup()`, which takes several optional arguments:
    - `x=0` is the starting x-value
    - `y=0` is the starting y-value
    - `feedrate=100` is the starting feedrate
    - `hotend_temp=215` is the default temp of the hotend
    - `bed_temp=60` is the default temp of the bed
- To write the finalization sequence to the output file, use `t.finish()` (which cools down the bed, moves the extruder up, etc)

### Turtle actions

Here are the basic built-in actions of the turtle:

- `t.move(distance)` moves the turtle forward a distance of `distance`, extruding along the way if the pen is down.
- `t.left(theta)` turns the turtle left by an angle `theta`.
- `t.right(theta)` turns the turtle right by an angle `theta`.
- `t.lift(height)` lifts the turtle up by a distance `height`. Usually used to move to the next layer of the print.
- `t.move_lift(distance, height)` moves the turtle forward by a distance `distance` and up by a distance `height`, extruding along the way if the pen is down.
- `t.penup()` lifts the pen up (extrusion will not occur until the pen is back down).
- `t.pendown()` puts the pen down (extrusion will occur until the pen is lifted up again).
- `t.do(command)` will write a manually-written custom GCODE command `command` to the output file.

### Configuration

The following functions are used to configure the turtle and the style of the print:

- `t.set_density(density)` sets the density of extrusion, that is, the ratio of mm filament extruded to mm moved by the turtle.
- `t.rate(feedrate)` sets the feedrate (think speed) of the turtle.

## Example code

In the `demos` folder, you can find a few snippets of example code using `ExtruderTurtle` to generate GCODE files for interesting 3D prints. Here are descriptions of these demos, in roughly increasing order of complexity:

- `seven_star.py`: draws a self-intersecting star polygon with seven points.
- `spiral.py`: draws a flat circle of plastic by tracing out a very tight spiral.
- `nonplanar_star.py`: draws the same star polygon as `seven_star.py`, but slightly concave down, so that the middle is higher than the points, using nonplanar slicing to make a smooth curve rather than one with stair-stepping
- `dreamcatcher.py`: creates a dreamcatcher-like design by tracing out a very thin cylinder filled with random chords.
- `snowflake_lsystem.py`: encodes the Koch Snowflake as an L-System with substitution rules, which it uses to generate a sequence of instructions for the turtle to follow to trace out the Snowflake
- `complex_walk.py`: uses the mathematical properties and symmetries of a certain class of walks in the complex plane to generate a beautiful shape.
- `evolving_snowflake.py`: draws the successive generations by which a Koch Snowflake fractal is produced, in such a way that they appear to "morph into" each other.
