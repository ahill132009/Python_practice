class OneIndexedList:
	def __init__(self, items=None):
		self.items = items or []

	def __getitem__(self, idx):
		if idx == 0 or idx > len(self.items):
			raise IndexError
		else:
			return self.items[idx-1]


o = OneIndexedList()
o.items.append(1)
print(o[1])
