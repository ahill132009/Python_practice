class OneIndexedList:
	def __init__(self, items=None):
		self.items = items or []

	def __getitem__(self, idx):
		if idx == 0 or idx > len(self.items):
			raise IndexError
		else:
			return self.items[idx-1]

	def __setitem__(self, key, value):
		self.items[key-1] = value
