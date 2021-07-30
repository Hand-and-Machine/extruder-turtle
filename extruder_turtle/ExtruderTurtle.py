import os
import math
import rhinoscriptsyntax as rs
__location__ = os.path.dirname(__file__)

class ExtruderTurtle:

    def __init__(self):
        self.out_filename = "turtle.gcode"
        self.initseq_filename = os.path.join(__location__, "data/initseqEnder.gcode")
        self.finalseq_filename = os.path.join(__location__, "data/finalseq.gcode")
        self.out_file = False;
        self.initseq_file = False;
        self.finalseq_file = False;
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.forward_vec = [1, 0, 0]
        self.left_vec = [0, 1, 0]
        self.up_vec = [0, 0, 1]
        self.use_degrees = False
    
        self.feedrate = 0
        self.density = 0.05
        self.pen = True

        self.write_gcode = True
        self.track_history = True
        self.prev_points = []
        self.line_segs = []
        self.extrusion_history = []

        self.G1xyze = "G1 X{x} Y{y} Z{z} E{e}"
        self.G1xyz = "G1 X{x} Y{y} Z{z}"
        self.G1xye = "G1 X{x} Y{y} E{e}"
        self.G1xy = "G1 X{x} Y{y}"
        self.G1e = "G1 E{e}"
        self.G1f = "G1 F{f}"
        self.G1z = "G1 Z{z}"
        self.G4p = "G4 P{p}"
        self.M0 = "M0"
        self.M104s = "M104 S{s}\nM109 S{s}"
        self.M140s = "M140 S{s}\nM190 S{s}"

    def convert_angle(self, angle):
        if self.use_degrees: return math.radians(angle)
        return angle

    def name(self, filename):
        self.out_filename = filename

    def do(self, cmd):
        if self.write_gcode:
            self.out_file.write(cmd + "\n")

    def setup(self, x=0,
                    y=0,
                    z=0,
                    feedrate=1000,
                    hotend_temp=205,
                    bed_temp=60,
                    filename=False
                    ):
        if self.track_history: self.prev_points = [(x,y,z)]
        if (filename):
            self.out_filename = filename
        self.x = x
        self.y = y
        self.z = z
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
        self.do(self.G1e.format(e=-3))

    def pendown(self):
        self.pen = True
        self.do(self.G1e.format(e=3))

    def yaw(self, angle):
        theta = self.convert_angle(angle)
        new_forward = [math.cos(theta)*self.forward_vec[i] + math.sin(theta)*self.left_vec[i] for i in range(3)]
        new_left = [math.cos(theta)*self.left_vec[i] - math.sin(theta)*self.forward_vec[i] for i in range(3)]
        self.forward_vec = new_forward
        self.left_vec = new_left

    def pitch(self, angle):
        theta = self.convert_angle(angle)
        new_forward = [math.cos(theta)*self.forward_vec[i] + math.sin(theta)*self.up_vec[i] for i in range(3)]
        new_up = [math.cos(theta)*self.up_vec[i] - math.sin(theta)*self.forward_vec[i] for i in range(3)]
        self.forward_vec = new_forward
        self.up_vec = new_up

    def roll(self, angle):
        theta = self.convert_angle(angle)
        new_left = [math.cos(theta)*self.left_vec[i] + math.sin(theta)*self.up_vec[i] for i in range(3)]
        new_up = [math.cos(theta)*self.up_vec[i] - math.sin(theta)*self.left_vec[i] for i in range(3)]
        self.left_vec = new_left
        self.up_vec = new_up

    def left(self, angle):
        self.yaw(angle)

    def right(self, angle):
        self.yaw(-angle)

    def pitch_up(self, angle):
        self.pitch(angle)

    def pitch_down(self, angle):
        self.pitch(-angle)

    def roll_left(self, angle):
        self.roll(-angle)

    def roll_right(self, angle):
        self.roll(angle)

    def set_heading(self, yaw, pitch=0, roll=0):
        self.forward_vec = [1, 0, 0]
        self.left_vec = [0, 1, 0]
        self.up_vec = [0, 0, 1]
        self.yaw(yaw)
        self.pitch(pitch)
        self.roll(roll)

    def change_heading(self, yaw=0, pitch=0, roll=0):
        self.set_heading(self.yaw + yaw, self.pitch + pitch, self.roll + roll)

    def rate(self, feedrate):
        self.do(self.G1f.format(f=feedrate))

    def record_move(self, dx, dy, dz, de=0):
        if self.track_history:
            prev_point = self.prev_points[-1]
            next_point = (prev_point[0]+dx, prev_point[1]+dy, prev_point[2]+dz) 
            self.prev_points.append(next_point)
            if self.pen: 
                self.line_segs.append([self.prev_points[-2], self.prev_points[-1]])
                self.extrusion_history.append(de)

    def forward(self, distance):
        extrusion = abs(distance) * self.density
        dx = distance * self.forward_vec[0]
        dy = distance * self.forward_vec[1]
        dz = distance * self.forward_vec[2]
        dx = round(dx, 5)
        dy = round(dy, 5)
        dz = round(dz, 5)
        self.x += dx
        self.y += dy
        self.z += dz
        self.record_move(dx, dy, dz, de=extrusion)
        if self.pen:
            self.do(self.G1xyze.format(x=dx, y=dy, z=dz, e=extrusion))
        else:
            self.do(self.G1xyz.format(x=dx, y=dy, z=dz))

    def forward_lift(self, distance, height):
        extrusion = math.sqrt(distance**2+height**2) * self.density
        dx = distance * self.forward_vec[0] + height * self.up_vec[0]
        dy = distance * self.forward_vec[1] + height * self.up_vec[1]
        dz = distance * self.forward_vec[2] + height * self.up_vec[2]
        dx = round(dx, 5)
        dy = round(dy, 5)
        dz = round(dz, 5)
        self.x += dx
        self.y += dy
        self.z += dz
        self.record_move(dx, dy, dz, de=extrusion)
        if self.pen:
            self.do(self.G1xyze.format(x=dx, y=dy, z=dz, e=extrusion))
        else:
            self.do(self.G1xyz.format(x=dx, y=dy, z=dz))

    def backward(self, distance):
        self.forward(-distance)

    def lift(self, height):
        self.do(self.G1z.format(z=height))
        self.z += height
        self.record_move(0, 0, height)

    def set_position(self, x=False, y=False, z=False):
        if x == False: x = self.x
        if y == False: y = self.y
        if z == False: z = self.z
        dx = round(x-self.x, 5)
        dy = round(y-self.y, 5)
        dz = round(z-self.z, 5)
        self.x = x
        self.y = y
        self.z = z
        distance = math.sqrt(dx*dx+dy*dy+dz*dz)
        extrusion = abs(distance) * self.density
        self.record_move(dx, dy, dz, de=extrusion)
        if self.pen:
            self.do(self.G1xyze.format(x=dx, y=dy, z=dz, e=extrusion))
        else:
            self.do(self.G1xyz.format(x=dx, y=dy, z=dz))

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z

    def get_yaw(self):
        x, y, z = self.forward_vec
        net_yaw = math.atan2(y, x)
        if self.use_degrees: return math.degrees(net_yaw)
        return net_yaw
    
    def get_pitch(self):
        x, y, z = self.forward_vec
        r = math.sqrt(x**2+y**2)
        net_pitch = math.atan2(z, r)
        if self.use_degrees: return math.degrees(net_pitch)
        return self.net_pitch
   
    def get_roll(self):
        net_yaw = self.get_yaw()
        net_pitch = self.get_pitch()
        if self.use_degrees:
            net_yaw = math.radians(net_yaw)
            net_pitch = math.radians(net_pitch)
        left_vech = [-math.sin(net_yaw), math.cos(net_yaw), 0]
        up_vech = [-math.sin(net_pitch)*math.cos(net_yaw), -math.sin(net_pitch)*math.sin(net_yaw), math.cos(net_pitch)]
        y = sum([self.left_vec[i]*up_vech[i] for i in range(3)])
        x = sum([self.left_vec[i]*left_vech[i] for i in range(3)])
        net_roll = math.atan2(y, x)
        if self.use_degrees: return math.degrees(net_roll)
        return self.net_roll

    def dwell(self, ms):
        self.do(self.G4p.format(p=ms))

    def draw_turtle(self):
        new_forward = [math.cos(math.radians(90))*self.forward_vec[i] + math.sin(math.radians(90))*self.left_vec[i] for i in range(3)]
        dx = 2 * new_forward[0]
        dy = 2 * new_forward[1]
        dz = 2 * new_forward[2]
        point1 = rs.AddPoint(self.getX()+dx, self.getY()+dy, self.getZ()+dz)
        new_forward = [math.cos(math.radians(-90))*self.forward_vec[i] + math.sin(math.radians(-90))*self.left_vec[i] for i in range(3)]
        dx = 2 * new_forward[0]
        dy = 2 * new_forward[1]
        dz = 2 * new_forward[2]
        point2 = rs.AddPoint(self.getX()+dx, self.getY()+dy, self.getZ()+dz)
        dx = 5 * self.forward_vec[0]
        dy = 5 * self.forward_vec[1]
        dz = 5 * self.forward_vec[2]
        point3 = rs.AddPoint(self.getX()+dx, self.getY()+dy, self.getZ()+dz)
        points = (point1, point2, point3)
        surface = rs.AddSrfPt(points)
        return surface

    def pause_and_wait(self):
        self.do(self.M0)

    def extrude(self, quantity):
        self.do(self.G1e.format(e=quantity))

    def bed_temp(self, temp):
        self.do(self.M140s.format(s=temp))

    def extruder_temp(self, temp):
        self.do(self.M104s.format(s=temp))

