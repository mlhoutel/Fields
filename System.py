from Point import *
from Wall import *
import numpy as np
import math as m

class System():
    def __init__(self, epsilon, gamma):
        self.points = []        # Array of Points
        self.walls = []         # Array of Walls
        self.epsilon = epsilon  # Permitivité
        self.gamma = gamma      # Conductivité

    def addPoint(self, point):
        self.points.append(point)

    def addWall(self, wall):
        self.walls.append(wall)
   
    def compute(self, i, X, Y, R, U):
        I = (U*self.gamma*2*np.pi)
        Sigma = (I*self.epsilon) / (self.gamma*4*np.pi*m.pow(R,2))
        
        dist = m.sqrt(m.pow(Y[i], 2) + m.pow(X[i], 2)) # Euclidean distance
        
        if (dist < R):
            return ((Sigma*m.pow(R, 2))/self.epsilon)*(1/R) # Constant when we are inside the point
        else:
            return ((Sigma*m.pow(R, 2))/self.epsilon)*(1/dist) 

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
            E = np.array([self.compute(i, tX, tY, point.size, point.tens) for i in range(size)], dtype=np.float)
            E.shape = (u, v)
            # E = np.pad(E,((shiftx,0),(0,shifty)), mode='constant')[:-shiftx,:-shifty]
            V = V + E
        
        return V