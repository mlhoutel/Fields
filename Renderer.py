import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from System import *
from Draggable import *

mpl.rcParams['toolbar'] = 'None' 

class Renderer():
    def __init__(self, system, XMAX, YMAX, density, rx, ry):
        self.system = system
        self.XMAX, self.YMAX = XMAX, YMAX
        self.density = density
        self.rx, self.ry = rx, ry

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
        V = self.system.field(X, Y)
        [Ex, Ey] = np.gradient(V, self.rx, self.ry)
        
        # Draw only if the field exists
        if len(Ex) and len(Ey):
            self.ax.streamplot(x, y, Ey, Ex, color=(2*np.log(np.hypot(Ex, Ey))), linewidth=1, cmap=plt.cm.inferno, density=self.density, arrowstyle='->', arrowsize=1.5)
            self.ax.matshow(V, interpolation='nearest', alpha=1, cmap=plt.cm.plasma, extent=(-self.XMAX, self.XMAX, self.YMAX, -self.YMAX))

    def dpoints(self):
        self.draggables = []
        for point in self.system.points:
            circle = Circle((point.x, point.y), point.size, color=plt.cm.RdBu(mpl.colors.Normalize(vmin=-10, vmax=10)(point.tens)), zorder=100)
            self.ax.add_patch(circle)
            draggable = Draggable(circle, self.update, point)
            draggable.connect()
            self.draggables.append(draggable)


    def dwalls(self):
        for wall in self.system.walls:
            self.ax.plot([wall.x1, wall.y1], [wall.x2, wall.y2], marker = 'o')