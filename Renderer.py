import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from System import *
from Draggable import *

class Renderer():
    def __init__(self):
        self.XMAX, self.YMAX = 0.6, 0.6
        self.density = 1.2
        self.rx, self.ry = 40, 40
        self.system = System()

    def launch(self):
        self.figure, self.ax = plt.subplots()
        self.update()
        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y$')
        self.ax.set_xlim(-self.XMAX, self.XMAX)
        self.ax.set_ylim(-self.YMAX, self.YMAX)
        self.ax.set_aspect('equal')
        plt.show()

    def update(self):
        self.clear()
        self.dfield()
        self.dpoints()
        self.dwalls()
    
    def clear(self):
        # self.ax = plt.gca()
        self.ax.patches = [] # clear lines streamplot
        self.ax.collections = [] # clear arrowheads streamplot

    def dfield(self):
        x = np.linspace(-self.XMAX, self.XMAX, self.rx)
        y = np.linspace(-self.YMAX, self.YMAX, self.ry)
        X, Y = np.meshgrid(x, y)
        [Ex, Ey] = self.system.field(X, Y, self.rx, self.ry)
        
        # Draw only if the field exists
        if len(Ex) and len(Ey):
            stream = self.ax.streamplot(x, y, Ex, Ey, color=(2*np.log(np.hypot(Ex, Ey))), linewidth=1, cmap=plt.cm.inferno, density=self.density, arrowstyle='->', arrowsize=1.5)

    def dpoints(self):
        self.draggables = []
        for point in self.system.points:
            circle = Circle((point.x, point.y), point.size, color='b', zorder=100)
            self.ax.add_patch(circle)
            draggable = Draggable(circle, self.update, point)
            draggable.connect()
            self.draggables.append(draggable)


    def dwalls(self):
        for wall in self.system.walls:
            print("wall")