class ReverseIter:
	"""docstring for ReverseIter"""
	def __init__(self, l):
		self.l = l
		self.n = len(l) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if 0 <= self.n:
			n = self.n
			self.n -= 1
			return self.l[n]
		else:
			raise StopIteration()


		