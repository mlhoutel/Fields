import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from System import *
from Draggable import *

# plt.ion()
class Renderer():
    def __init__(self):
        self.XMAX, self.YMAX = 40, 40
        self.nx, self.ny = 64, 64
        self.system = System()
        self.system.addPoint(Point(0, 0, 3))

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
        self.system.update()

        self.dfield()
        self.dpoints()
        self.dwalls()
        
        # self.figure.canvas.draw()
        # self.figure.canvas.flush_events()
    
    def dfield(self):
        x = np.linspace(-self.XMAX, self.XMAX, self.nx)
        y = np.linspace(-self.YMAX, self.YMAX, self.ny)
        X, Y = np.meshgrid(x, y)
        [Bx, By] = self.system.field(X, Y)
        color = 2 * np.log(np.hypot(Bx, By))
        self.ax.streamplot(x, y, Bx, By, color=color, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle='->', arrowsize=1.5)


    def dpoints(self):
        for point in self.system.points:
            circle = Circle((point.x, point.y), point.size, color='b', zorder=100)
            self.ax.add_patch(circle)
            draggable = Draggable(circle)
            draggable.connect()

    def dwalls(self):
        for point in self.system.points:
            print("wall")

Renderer()