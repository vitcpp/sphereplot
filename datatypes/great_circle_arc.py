from .point import Point

class GreatCircleArc:

	def __init__(self, beg : Point, end : Point):
		self.pts = [beg, end]

	def __getitem__(self, idx):
		return self.pts[idx]
