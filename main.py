from Renderer import *

renderer = Renderer()
renderer.system.addPoint(Point(-0.3, -0.3, 0.03, 0.55, 2))
renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, -2))
renderer.launch()