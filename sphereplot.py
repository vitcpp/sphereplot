import numpy as np
import matplotlib.pyplot as plt

class Point:

	def __init__(self, lng, lat):
		self.coords = [lng, lat]

	def __getitem__(self, idx):
		return self.coords[idx]

class Vector:

	def __init__(self, data, color = None):
		if isinstance(data, Point):
			self.coords = [
				np.cos(data[0]) * np.cos(data[1]),
				np.sin(data[0]) * np.cos(data[1]),
				np.sin(data[1])
				]
		elif isinstance(data, list):
			self.coords = np.array(data)
		elif isinstance(data, np.ndarray):
			self.coords = data.copy()
		self.color = "black" if color is None else color

	def __getitem__(self, idx):
		return self.coords[idx]

	def cross_product(self, v):
		x = self[1] * v[2] - self[2] * v[1]
		y = self[2] * v[0] - self[0] * v[2]
		z = self[0] * v[1] - self[1] * v[0]
		return Vector([x, y, z])

	def dot_product(self, v):
		return self[0] * v[0] + self[1] * v[1] + self[2] * v[2];

	def normalized(self):
		norm = np.sqrt(self[0] ** 2 + self[1] ** 2 + self[2] ** 2)
		coords = self.coords / norm
		return Vector(coords)

class GreatCircleArc:

	def __init__(self, beg : Point, end : Point):
		self.pts = [beg, end]

	def __getitem__(self, idx):
		return self.pts[idx]

class Meridian:

	def __init__(self, lng):
		self.lng = lng

class Parallel:

	def __init__(self, lat):
		self.lat = lat

class Scene:

	def __init__(self, fig, rect):
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
		self.axes.view_init(elev=45., azim=15)
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
		lngv = gobj.lng
		latv = np.linspace(-np.pi/2, np.pi/2, 100)
		x = np.cos(lngv) * np.cos(latv)
		y = np.sin(lngv) * np.cos(latv)
		z = np.sin(latv)
		self.axes.scatter(x, y, z, **kwargs)

	def __plot_parallel(self, gobj):
		lngv = np.linspace(0, 2 * np.pi, 100)
		latv = gobj.lat
		x = np.cos(lngv) * np.cos(latv)
		y = np.sin(lngv) * np.cos(latv)
		z = np.sin(latv)
		self.axes.scatter(x, y, z, s = 0.1, color = "darkgray")

	def __plot_arc(self, garc, **kwargs):
		v1 = Vector(garc[0])
		v2 = Vector(garc[1])
		v3 = v1.cross_product(v2)
		v4 = v3.cross_product(v2).normalized()
		dp = -np.arccos(v1.dot_product(v2))
		t = np.linspace(0, dp, 1000)
		x = np.cos(t) * v2[0] + np.sin(t) * v4[0]
		y = np.cos(t) * v2[1] + np.sin(t) * v4[1]
		z = np.cos(t) * v2[2] + np.sin(t) * v4[2]
		k = { "color" : "red", "s" : 0.1 } | kwargs
		self.axes.scatter(x, y, z, **k)

	def __plot_vector(self, gvec : Vector, **kwargs):
		x = np.linspace(0, gvec[0], 100)
		y = np.linspace(0, gvec[1], 100)
		z = np.linspace(0, gvec[2], 100)
		self.axes.plot3D(x, y, z, **kwargs)
