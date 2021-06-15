from Renderer import *

system = System(8.85418782e-12, 0.04)
renderer = Renderer(system, 1.6, 1.6, 1.6, 200, 200)

renderer.system.addPoint(Point(-0.5, 0.0, 0.02, 0.55, 10))
renderer.system.addPoint(Point(-0.35, 0.0, 0.02, 0.55, -10))
renderer.system.addPoint(Point(0.35, 0.0, 0.02, 0.55, -10))
renderer.system.addPoint(Point(0.5, 0.0, 0.02, 0.55, 10))
# renderer.system.addPoint(Point(0.3, 0.3, 0.03, 0.55, 0.5))
# renderer.system.addWall(Wall(-0.6, 0.6, 0.6, -0.6))

renderer.launch()