import numpy as np
from .point import Point

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

	def points(self, num : int):
		x = np.linspace(0, self[0], num)
		y = np.linspace(0, self[1], num)
		z = np.linspace(0, self[2], num)
		return x, y, z
