from sphereplot import *

fig = plt.figure(figsize = (5, 5))

sphere = Sphere(fig, rect = [0, 0, 1, 1], camera = (0, 0))

sphere.parallel(0)
sphere.parallel(1)
sphere.parallel(np.pi/2)
sphere.parallel(-1)
sphere.parallel(-np.pi/2)

for lng in np.linspace(0, 2* np.pi, 16):
	sphere.meridian(lng, s = 0.1, color = "gray")

sphere.vector(0, 1, color="blue")
sphere.vector(1, 1, color="blue")

sphere.great_circle_arc(0, 0, 0, 1)
sphere.great_circle_arc(0, 1, 1, 1, color = "yellow")
sphere.great_circle_arc(1, 1, 1, 0)
sphere.great_circle_arc(1, 0, 0, 0)

#sphere.camera(35, 45)

plt.show()
