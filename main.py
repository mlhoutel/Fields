from Renderer import *

renderer = Renderer()
renderer.system.addPoint(Point(-0.3, -0.3, 0.03, 0.55, 2))
renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, -2))
renderer.system.addWall(Wall(0, 0, 0.2, 0.1))
renderer.launch()