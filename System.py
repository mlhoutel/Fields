from Point import *
from Wall import *
import numpy as np
import math as m

class System():
    def __init__(self):
        self.points = []
        self.walls = []
        self.epsilon = 8.85418782e-12   # Permitivité
        self.gamma = 0.04               # Conductivité

    def addPoint(self, point):
        self.points.append(point)

    def addWall(self, wall):
        self.walls.append(wall)
   
    def compute(self, i, X, Y, R, L, U):
        I = (U*self.gamma*2*np.pi)
        Sigma = (I*self.epsilon) / (self.gamma*4*np.pi*m.pow(R,2))
        
        R1 = m.sqrt(m.pow(L/2 + 0.1, 2) + m.pow(Y[i], 2) + m.pow(X[i], 2))
        R2 = m.sqrt(m.pow(L/2 - 0.1, 2) + m.pow(Y[i], 2) + m.pow(X[i], 2))
        
        if (R1 < R):
            return ((Sigma*m.pow(R, 2))/self.epsilon)*(1/R - 1/L)
        elif (R2 < R):
            return -((Sigma*m.pow(R, 2))/self.epsilon)*(1/R - 1/L)
        else:
            return ((Sigma*m.pow(R, 2))/self.epsilon)*(1/R1 - 1/R2)

    def field(self, X, Y):
        u, v = X.shape
        size = np.size(X)
        X.shape = (size)
        Y.shape = (size)
        V = np.zeros((u, v))

        for point in self.points:
            # Loop shifting: removed for a better shifting
            # shiftx = int(round(point.x / ((X[-1] - X[1])/dx)))
            # shifty = int(round(point.y / ((X[-1] + X[1])/dy)))
            # tX = np.concatenate((X[-shiftx:], X[:-shiftx]))
            # tY = np.concatenate((Y[-shifty:], Y[:-shifty]))

            tX = [X[i]-point.x for i in range(np.size(X))]
            tY = [Y[i]-point.y for i in range(np.size(Y))]
            E = np.array([self.compute(i, tX, tY, point.size, point.dist, point.tens) for i in range(size)], dtype=np.float)
            E.shape = (u, v)
            # E = np.pad(E,((shiftx,0),(0,shifty)), mode='constant')[:-shiftx,:-shifty]
            V = V + E
        
        return V