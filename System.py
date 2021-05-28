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
        # for point in self.points:

    def B(self, r, theta):
        # Mean magnitude of the Earth's magnetic field at the equator in T
        B0 = 3.12e-5
        # Radius of Earth, Mm (10^6 m: mega-metres!)
        RE = 6.370
        # Deviation of magnetic pole from axis
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
        c, s = np.cos(np.pi/2 + theta), np.sin(np.pi/2 + theta)
        Bx = -Btheta * s + Br * c
        By = Btheta * c + Br * s
        # ------------------------------- TEMP ------------------------------- #
        
        return [Bx, By]