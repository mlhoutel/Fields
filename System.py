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

    # temp function
    def B(self, r, theta):
        B0 = 3.12e-5
        RE = 6.370
        alpha = np.radians(9.6)

        """Return the magnetic field vector at (r, theta)."""
        fac = B0 * (RE / r)**3
        return -2 * fac * np.cos(theta + alpha), -fac * np.sin(theta + alpha)

    def field(self, X, Y):
        # ------------------------------- TEMP ------------------------------- #
        r, theta = np.hypot(X, Y), np.arctan2(Y, X)

        # Magnetic field vector, B = (Ex, Ey), as separate components
        Br, Btheta = self.B(r, theta)

        # Transform to Cartesian coordinates: NB make North point up, not to the right.
        c, s = np.cos(np.pi/2 + theta + self.points[0].x), np.sin(np.pi/2 + theta)
        Bx = -Btheta * s + Br * c
        By = Btheta * c + Br * s
        # ------------------------------- TEMP ------------------------------- #
        
        return [Bx, By]