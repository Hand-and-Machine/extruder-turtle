import os
import math
from .location import __location__

class ExtruderTurtle:

    def __init__(self):
        self.out_filename = "turtle.gcode"
        self.initseq_filename = os.path.join(__location__, "data/initseq.gcode")
        self.finalseq_filename = os.path.join(__location__, "data/finalseq.gcode")
        self.out_file = False;
        self.initseq_file = False;
        self.finalseq_file = False;
        self.heading = 0
        self.feedrate = 0
        self.density = 0.05
        self.pendown = True;
        self.G1xyze = "G1 X{x} Y{y} Z{z} E{e}"
        self.G1xyz = "G1 X{x} Y{y} Z{z}"
        self.G1xye = "G1 X{x} Y{y} E{e}"
        self.G1xy = "G1 X{x} Y{y}"
        self.G1f = "G1 F{f}"
        self.G1z = "G1 Z{z}"

    def name(self, filename):
        self.out_filename = filename

    def do(self, cmd):
        self.out_file.write(cmd + "\n")

    def setup(self, x=0,
                    y=0,
                    feedrate=1000,
                    hotend_temp=215,
                    bed_temp=60
                    ):
        self.out_file = open(self.out_filename, 'w+')
        self.initseq_file = open(self.initseq_filename, 'r')
        self.do(self.initseq_file.read().format(**locals()))
        self.initseq_file.close()

    def finish(self):
        self.finalseq_file = open(self.finalseq_filename, 'r')
        self.do(self.finalseq_file.read())
        self.finalseq_file.close()
        self.out_file.close()

    def set_density(self, density):
        self.density = density

    def penup(self):
        self.pendown = False

    def pendown(self):
        self.pendown = True

    def rate(self, feedrate):
        self.do(self.G1f.format(f=feedrate))

    def right(self, theta):
        self.heading += theta
        self.heading = self.heading % (2*math.pi)

    def left(self, theta):
        self.heading += -theta
        self.heading = self.heading % (2*math.pi)

    def move(self, distance):
        extrusion = distance * self.density
        dx = distance * math.cos(self.heading)
        dy = distance * math.sin(self.heading)
        if self.pendown:
            self.do(self.G1xye.format(x=dx, y=dy, e=extrusion))
        else:
            self.do(self.G1xy.format(x=dx, y=dy))

    def move_lift(self, distance, height):
        extrusion = self.density * (distance**2 + height**2)**(1/2)
        dx = distance * math.cos(self.heading)
        dy = distance * math.sin(self.heading)
        if self.pendown:
            self.do(self.G1xyze.format(x=dx, y=dy, z=height, e=extrusion))
        else:
            self.do(self.G1xyz.format(x=dx, y=dy, z=height))

    def lift(self, height):
        self.do(self.G1z.format(z=height))
