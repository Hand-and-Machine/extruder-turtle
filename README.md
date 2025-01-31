# OUTDATED USE EXTRUDER TURTLE RHINO


# extruder-turtle

A Python package that uses the principles of 3D Turtle Geometry to generate GCODE for 3D-printed solids.

## Basic functionality

The `ExtruderTurtle` class is very simple, and only has a few built-in functions implementing the basic functionality of a turtle.

### Setup

Here are several methods of the `ExtruderTurtle` class that are used to set up your turtle:

- The constructor `t = ExtruderTurtle()` which takes no arguments. The turtle is constructed with a few default values in place:
    - The default output file name `turtle.gcode`
    - Default starting orientation, consisting of three vectors: `forward_vec` (which you may imagine as pointing out of the turtle's nose), `up_vec` (normal to the turtle's shell), and `left_vec` (pointing out of the turtle's left side).
    - Default starting `feedrate` (the rate of movement) is `0`.
    - Default starting `density` (ratio of mm extruded to mm moved) is `0`.
    - Default starting `pendown` value (whether or not the turtle extrudes while moving) is `True`.
- To change the name of the output file, use `t.name("your-filename.gcode")`.
- To write the initialization sequence (which moves the turtle to the initial position, runs the mesh bed leveling, heats the bed and extruder, etc) to the output file, run `t.setup()`, which takes several optional arguments:
    - `x=0` is the starting x-value
    - `y=0` is the starting y-value
    - `feedrate=100` is the starting feedrate
    - `hotend_temp=215` is the default temp of the hotend
    - `bed_temp=60` is the default temp of the bed
- To write the finalization sequence to the output file, use `t.finish()` (which cools down the bed, moves the extruder up, etc).

### Turtle actions

Here are the basic built-in actions of the turtle:

- `t.forward(distance)` moves the turtle forward a distance of `distance`, extruding along the way if the pen is down.
- `t.left(theta)` turns the turtle left by an angle `theta`. This is just an easier-to-remember alias for `t.yaw(theta)`.
- `t.right(theta)` turns the turtle right by an angle `theta`. Alias for `t.yaw(-theta)`.
- `t.pitch_up(theta)` tilts the turtle "upwards" in the direction where its eyes would point. Alias for `t.pitch(theta)`.
- `t.pitch_down(theta)` tilts the turtle "downwards". Alias for `t.pitch(-theta)`.
- `t.roll_left(theta)` rolls the turtle towards its left side. Alias for `t.roll(-theta).
- `t.roll_right(theta)` rolls the turtle towards its right side. Alias for `t.roll(theta)`.
- `t.lift(height)` lifts the turtle up by a distance `height`. Usually used to move to the next layer of the print.
- `t.forward_lift(distance, height)` moves the turtle forward by a distance `distance` and up by a distance `height`, extruding along the way if the pen is down. Note that "up" here refers to the direction normal to the turtle's shell, not necessarily in the positive-z direction.
- `t.penup()` lifts the pen up (extrusion will not occur until the pen is back down).
- `t.pendown()` puts the pen down (extrusion will occur until the pen is lifted up again).
- `t.do(command)` will write a manually-written custom GCODE command `command` to the output file.

### Configuration

The following functions are used to configure the turtle and the style of the print:

- `t.set_density(density)` sets the density of extrusion, that is, the ratio of mm filament extruded to mm moved by the turtle.
- `t.rate(feedrate)` sets the feedrate (think speed) of the turtle.
- `t.track_history` is a boolean value, default `False`, which, when true, stores a list of all points previously visited by the turtle, and all line segments on which extrusion occurred. This is used primarily for visualization.

### Visualization

You may use Rhino/Grasshopper to visualize a preview of your 3D print before sending it to your printer, if you wish. 

The extruder_turtle library does not make use of any libraries that require distributions later than Python 2.7, so it can be used with RhinoPython. However, it needs to be installed separately, in a special directory containing Python packages used by Rhino/Grasshopper. On Mac OS, RhinoPython libraries are installed in the directory

`/Users/YOUR_USERNAME/Applications/Rhino\ 7.app/Contents/Frameworks/RhCore.framework/Versions/Current/Resources/ManagedPlugIns/RhinoDLR_Python.rhp/Lib`

You can simply save a copy of `ExtruderTurtleForRhino.py` to the `Lib` folder, and you should be able to use it from within Grasshopper. (Note: this is not the same as `ExtruderTurtle.py`, which is the source code that is used when you import the library in a code file outside of Rhino.) You may also need to add a folder called `data` containing `initseq.gcode` and `finalseq.gcode`, since these files are necessary for using the turtle to generate GCODE. Note that you may need to run Rhino as admin in order for it to have permission to open these files while running.

An example visualization with Grasshopper is given in `turtletest.gh` in the `demos` folder (it shows how to visualize an example identical to the one generated in `demos/seven_star.py`).

## Example code

In the `demos` folder, you can find a few snippets of example code using `ExtruderTurtle` to generate GCODE files for interesting 3D prints. Here are descriptions of these demos, in roughly increasing order of complexity:

- `seven_star.py`: draws a self-intersecting star polygon with seven points.
- `spiral.py`: draws a flat circle of plastic by tracing out a very tight spiral.
- `nonplanar_star.py`: draws the same star polygon as `seven_star.py`, but slightly concave down, so that the middle is higher than the points, using nonplanar slicing to make a smooth curve rather than one with stair-stepping
- `dreamcatcher.py`: creates a dreamcatcher-like design by tracing out a very thin cylinder filled with random chords.
- `snowflake_lsystem.py`: encodes the Koch Snowflake as an L-System with substitution rules, which it uses to generate a sequence of instructions for the turtle to follow to trace out the Snowflake
- `complex_walk.py`: uses the mathematical properties and symmetries of a certain class of walks in the complex plane to generate a beautiful shape.
- `evolving_snowflake.py`: draws the successive generations by which a Koch Snowflake fractal is produced, in such a way that they appear to "morph into" each other.
