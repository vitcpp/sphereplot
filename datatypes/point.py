
class Point:

	def __init__(self, lng, lat):
		self.coords = [lng, lat]

	def __getitem__(self, idx):
		return self.coords[idx]
