
# 1 
def integers():	
	a = 0
	while True:
		yield a
		a += 1

# 2
def squares(generator_from_foo):
	for i in generator_from_foo:
		yield i**2

# 3
def take(n, generator_from_foo):
	try:
		l = []
		for _ in range(n):
			l.append(next(generator_from_foo))
		return l
	except StopIteration:
		return l


# Make iterators
integer = integers()
square_gen = squares(integer)

print(take(10, square_gen))
