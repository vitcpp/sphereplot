import numpy as np
from .point import Point

class Parallel:

	def __init__(self, lat):
		self.lat = lat

	def points(self, num : int):
		lngv = np.linspace(0, 2 * np.pi, num)
		latv = self.lat
		x = np.cos(lngv) * np.cos(latv)
		y = np.sin(lngv) * np.cos(latv)
		z = np.sin(latv)
		return x, y, z
