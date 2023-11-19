import numpy as np
import matplotlib.pyplot as plt
from datatypes import *

class Sphere:

	def __init__(self, fig, rect, camera = None):
		self.fig = fig
		self.axes = self.fig.add_axes(projection = "3d", rect = rect)
		self.axes.grid(False)
		self.axes.set_xlim(-1, 1)
		self.axes.set_ylim(-1, 1)
		self.axes.set_zlim(-1, 1)
		self.axes.set(xticklabels=[], yticklabels=[], zticklabels=[])
		self.axes.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		self.axes.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		self.axes.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		self.axes._axis3don = False
		self.axes.set_aspect("equal");
		if camera is None:
			self.axes.view_init(elev=45., azim=15)
		else:
			self.axes.view_init(camera[0], camera[1])
		self.__plot_axes()

	def camera(self, elev, azim):
		self.axes.view_init(elev = elev, azim = azim)

	def plot(self, gobj):
		self.__plot_object(gobj)

	def parallel(self, lat, **kwargs):
		self.__plot_parallel(Parallel(lat), **kwargs)

	def meridian(self, lng, **kwargs):
		self.__plot_meridian(Meridian(lng), **kwargs)

	def vector(self, lng, lat, **kwargs):
		self.__plot_vector(Vector(Point(lng, lat)), **kwargs)

	def great_circle_arc(self, lng1, lat1, lng2, lat2, **kwargs):
		self.__plot_arc(GreatCircleArc(Point(lng1, lat1), Point(lng2, lat2)), **kwargs)

	def __plot_axes(self):
		val = [1,0,0]
		labels = ['x', 'y', 'z']
		colors = ['r', 'g', 'b']
		for v in range(3):
			x = [val[v-0], -val[v-0]]
			y = [val[v-1], -val[v-1]]
			z = [val[v-2], -val[v-2]]
			self.axes.plot(x, y, z,'-', linewidth=1)
			self.axes.text(val[v-0], val[v-1], val[v-2], labels[v], color=colors[v], fontsize=12)

	def __plot_object(self, gobj):
		if isinstance(gobj, Meridian):
			self.__plot_meridian(gobj)
		elif isinstance(gobj, Parallel):
			self.__plot_parallel(gobj)
		elif isinstance(gobj, GreatCircleArc):
			self.__plot_arc(gobj)
		elif isinstance(gobj, Vector):
			self.__plot_vector(gobj)

	def __plot_meridian(self, gobj, **kwargs):
		x, y, z = gobj.points(100)
		self.axes.scatter(x, y, z, **kwargs)

	def __plot_parallel(self, gobj):
		x, y, z = gobj.points(200)
		self.axes.scatter(x, y, z, s = 0.1, color = "darkgray")

	def __plot_arc(self, garc, **kwargs):
		x, y, z = garc.points(100)
		k = { "color" : "red", "s" : 0.1 } | kwargs
		self.axes.scatter(x, y, z, **k)

	def __plot_vector(self, gvec : Vector, **kwargs):
		x, y, z = gvec.points(2)
		self.axes.plot3D(x, y, z, **kwargs)
