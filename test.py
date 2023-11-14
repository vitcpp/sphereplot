from sphereplot import *

scene = Scene()

scene.add(Equatorial(0))
scene.add(Equatorial(1))
scene.add(Equatorial(np.pi/2))
scene.add(Equatorial(-1))
scene.add(Equatorial(-np.pi/2))

for lng in np.linspace(0, 2* np.pi, 16):
	scene.add(Meridian(lng))

# scene.add(GreatCircleArc(Point(0, 1), Point(1, 1)))

scene.add(Vector(Point(0, 1), color="blue"))
scene.add(Vector(Point(1, 1), color="blue"))

scene.add(GreatCircleArc(Point(0, 0), Point(0, 1)))
scene.add(GreatCircleArc(Point(0, 1), Point(1, 1)))
scene.add(GreatCircleArc(Point(1, 1), Point(1, 0)))
scene.add(GreatCircleArc(Point(1, 0), Point(0, 0)))

scene.show()
