import numpy as np
from .point import Point
from .vector import Vector

class GreatCircleArc:

	def __init__(self, beg : Point, end : Point):
		self.pts = [beg, end]

	def __getitem__(self, idx):
		return self.pts[idx]

	def points(self, num : int):
		v1 = Vector(self[0])
		v2 = Vector(self[1])
		v3 = v1.cross_product(v2)
		v4 = v3.cross_product(v2).normalized()
		dp = -np.arccos(v1.dot_product(v2))
		t = np.linspace(0, dp, 1000)
		x = np.cos(t) * v2[0] + np.sin(t) * v4[0]
		y = np.cos(t) * v2[1] + np.sin(t) * v4[1]
		z = np.cos(t) * v2[2] + np.sin(t) * v4[2]
		return x, y, z
