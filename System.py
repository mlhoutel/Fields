from Point import *
from Wall import *
import numpy as np

class System():
    def __init__(self):
        self.points = []
        self.walls = []

    def addPoint(self, point):
        self.points.append(point)

    def addWall(self, wall):
        self.points.append(wall)

    def update(self):
        print("update")

    def field(self, X, Y):
        Bx = []
        By = []
        # TODO
        return [Bx, By]