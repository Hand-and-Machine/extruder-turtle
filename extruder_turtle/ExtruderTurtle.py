import os
import math
__location__ = os.path.dirname(__file__)

class ExtruderTurtle:

    def __init__(self):
        self.out_filename = "turtle.gcode"
        self.initseq_filename = os.path.join(__location__, "data/initseq.gcode")
        self.finalseq_filename = os.path.join(__location__, "data/finalseq.gcode")
        self.out_file = False;
        self.initseq_file = False;
        self.finalseq_file = False;
        
        self.forward_vec = [1, 0, 0]
        self.left_vec = [0, 1, 0]
        self.up_vec = [0, 0, 1]
        self.feedrate = 0
        self.density = 0.05
        self.pen = True

        self.write_gcode = True
        self.track_history = False
        self.prev_points = []
        self.line_segs = []

        self.G1xyze = "G1 X{x} Y{y} Z{z} E{e}"
        self.G1xyz = "G1 X{x} Y{y} Z{z}"
        self.G1xye = "G1 X{x} Y{y} E{e}"
        self.G1xy = "G1 X{x} Y{y}"
        self.G1e = "G1 E{e}"
        self.G1f = "G1 F{f}"
        self.G1z = "G1 Z{z}"
        self.G4p = "G4 P{p}"

    def name(self, filename):
        self.out_filename = filename

    def do(self, cmd):
        if self.write_gcode:
            self.out_file.write(cmd + "\n")

    def setup(self, x=0,
                    y=0,
                    feedrate=1000,
                    hotend_temp=215,
                    bed_temp=60
                    ):
        if self.track_history: self.prev_points = [(x,y,0)]
        if self.write_gcode:
            self.out_file = open(self.out_filename, 'w+')
            self.initseq_file = open(self.initseq_filename, 'r')
            self.do(self.initseq_file.read().format(**locals()))
            self.initseq_file.close()

    def finish(self):
        if self.write_gcode:
            self.finalseq_file = open(self.finalseq_filename, 'r')
            self.do(self.finalseq_file.read())
            self.finalseq_file.close()
            self.out_file.close()

    def set_density(self, density):
        self.density = density

    def penup(self):
        self.pen = False

    def pendown(self):
        self.pen = True

    def yaw(self, theta):
        new_forward = [math.cos(theta)*self.forward_vec[i] + math.sin(theta)*self.left_vec[i] for i in range(3)]
        new_left = [math.cos(theta)*self.left_vec[i] - math.sin(theta)*self.forward_vec[i] for i in range(3)]
        self.forward_vec = new_forward
        self.left_vec = new_left

    def pitch(self, theta):
        new_forward = [math.cos(theta)*self.forward_vec[i] + math.sin(theta)*self.up_vec[i] for i in range(3)]
        new_up = [math.cos(theta)*self.up_vec[i] - math.sin(theta)*self.forward_vec[i] for i in range(3)]
        self.forward_vec = new_forward
        self.up_vec = new_up

    def roll(self, theta):
        new_left = [math.cos(theta)*self.left_vec[i] + math.sin(theta)*self.up_vec[i] for i in range(3)]
        new_up = [math.cos(theta)*self.up_vec[i] - math.sin(theta)*self.left_vec[i] for i in range(3)]
        self.left_vec = new_left
        self.up_vec = new_up

    def rate(self, feedrate):
        self.do(self.G1f.format(f=feedrate))

    def record_move(self, dx, dy, dz=0):
        if self.track_history:
            prev_point = self.prev_points[-1]
            next_point = (prev_point[0]+dx, prev_point[1]+dy, prev_point[2]+dz) 
            self.prev_points.append(next_point)
            if self.pen: self.line_segs.append([self.prev_points[-2], self.prev_points[-1]])

    def forward(self, distance):
        extrusion = distance * self.density
        dx = distance * math.cos(self.heading)
        dy = distance * math.sin(self.heading)
        self.record_move(dx, dy)
        if self.pen:
            self.do(self.G1xye.format(x=dx, y=dy, e=extrusion))
        else:
            self.do(self.G1xy.format(x=dx, y=dy))

    def move_lift(self, distance, height):
        extrusion = self.density * (distance**2 + height**2)**(1/2)
        dx = distance * math.cos(self.heading)
        dy = distance * math.sin(self.heading)
        self.record_move(dx, dy, dz=height)
        if self.pen:
            self.do(self.G1xyze.format(x=dx, y=dy, z=height, e=extrusion))
        else:
            self.do(self.G1xyz.format(x=dx, y=dy, z=height))

    def lift(self, height):
        self.do(self.G1z.format(z=height))
        self.record_move(0, 0, dz=height)

    def dwell(self, ms):
        self.do(self.G4p.format(p=ms))

    def extrude(self, quantity):
        self.do(self.G1e.format(e=quantity))
