import os
import math
import rhinoscriptsyntax as rs
from extruder_turtle import *
__location__ = os.path.dirname(__file__)

class ExtruderTurtleForRhino(ExtruderTurtle):

    def __init__(self):
        super().__init__()

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
