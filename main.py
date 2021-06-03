from Renderer import *

renderer = Renderer()
renderer.system.addPoint(Point(-0.3, -0.3, 0.03, 0.55, 10))
renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, 7))
renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, 6))
renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, -10))
renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, -12))
# renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, 0.5))
# renderer.system.addWall(Wall(-0.6, 0.6, 0.6, -0.6))
renderer.launch()