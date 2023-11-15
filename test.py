from sphereplot import *

fig = plt.figure(figsize = (5, 5))

scene = Scene(fig, rect = [0, 0, 1, 1])

scene.parallel(0)
scene.parallel(1)
scene.parallel(np.pi/2)
scene.parallel(-1)
scene.parallel(-np.pi/2)

for lng in np.linspace(0, 2* np.pi, 16):
	scene.meridian(lng, s = 0.1, color = "gray")

scene.vector(0, 1, color="blue")
scene.vector(1, 1, color="blue")

scene.great_circle_arc(0, 0, 0, 1)
scene.great_circle_arc(0, 1, 1, 1, color = "yellow")
scene.great_circle_arc(1, 1, 1, 0)
scene.great_circle_arc(1, 0, 0, 0)

scene.camera(35, 45)

plt.show()
