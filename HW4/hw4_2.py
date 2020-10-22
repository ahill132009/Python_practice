class ReverseIter:
	"""docstring for ReverseIter"""
	def __init__(self, l):
		self.l = l
		self.n = len(l) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.n >= 0:
			new = self.n
			self.n -= 1
			return self.l[new]
		else:
			raise StopIteration


ll = ReverseIter([1,2,3,4,5])
print(next(ll))
print(next(ll))
print(next(ll))
print(next(ll))	
print(next(ll))	
print(next(ll))		