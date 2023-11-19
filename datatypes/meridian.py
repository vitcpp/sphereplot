import numpy as np
from .point import Point

class Meridian:

	def __init__(self, lng : float):
		self.lng = lng

	def points(self, num : int):
		lngv = self.lng
		latv = np.linspace(-np.pi/2, np.pi/2, num)
		x = np.cos(lngv) * np.cos(latv)
		y = np.sin(lngv) * np.cos(latv)
		z = np.sin(latv)
		return x, y, z
