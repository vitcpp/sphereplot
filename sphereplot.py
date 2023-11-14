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
		if idx == 0:
			return self.pts[0]
		elif idx == 1:
			return self.pts[1]
		assert False
		return None

class Meridian:

	def __init__(self, lng):
		self.lng = lng

class Equatorial:

	def __init__(self, lat):
		self.lat = lat

class Scene:

	def __init__(self):
		self.objects = []

	def add(self, gobj):
		self.objects.append(gobj)

	def plot(self):
		fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(20,20))
		self.fig = fig
		self.axes = ax
		ax.grid(False)
		ax.set_xlim(-1, 1)
		ax.set_ylim(-1, 1)
		ax.set_zlim(-1, 1)
		ax.set(xticklabels=[], yticklabels=[], zticklabels=[])
		ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		ax._axis3don = False
		ax.set_aspect("equal");
		ax.view_init(elev=45., azim=15)
		self.__plot_axes()
		self.__plot_objects()

	def show(self):
		self.plot()
		plt.show()

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

	def __plot_objects(self):
		for gobj in self.objects:
			self.__plot_object(gobj)

	def __plot_object(self, gobj):
		if isinstance(gobj, Meridian):
			self.__plot_meridian(gobj)
		elif isinstance(gobj, Equatorial):
			self.__plot_equatorial(gobj)
		elif isinstance(gobj, GreatCircleArc):
			self.__plot_arc(gobj)
		elif isinstance(gobj, Vector):
			self.__plot_vector(gobj)

	def __plot_meridian(self, gobj):
		lngv = gobj.lng
		latv = np.linspace(-np.pi/2, np.pi/2, 100)
		x = np.cos(lngv) * np.cos(latv)
		y = np.sin(lngv) * np.cos(latv)
		z = np.sin(latv)
		self.axes.scatter(x, y, z, s = 0.1, color = "darkgray")

	def __plot_equatorial(self, gobj):
		lngv = np.linspace(0, 2 * np.pi, 100)
		latv = gobj.lat
		x = np.cos(lngv) * np.cos(latv)
		y = np.sin(lngv) * np.cos(latv)
		z = np.sin(latv)
		self.axes.scatter(x, y, z, s = 0.1, color = "darkgray")

	def __plot_arc(self, garc):
		v1 = Vector(garc[0])
		v2 = Vector(garc[1])
		v3 = v1.cross_product(v2)
		v4 = v3.cross_product(v2).normalized()
		dp = -np.arccos(v1.dot_product(v2))
		t = np.linspace(0, dp, 1000)
		x = np.cos(t) * v2[0] + np.sin(t) * v4[0]
		y = np.cos(t) * v2[1] + np.sin(t) * v4[1]
		z = np.cos(t) * v2[2] + np.sin(t) * v4[2]
		self.axes.scatter(x, y, z, s = 0.1, color = "red")

	def __plot_vector(self, gvec : Vector):
		x = np.linspace(0, gvec[0], 100)
		y = np.linspace(0, gvec[1], 100)
		z = np.linspace(0, gvec[2], 100)
		self.axes.plot3D(x, y, z, color = gvec.color)
