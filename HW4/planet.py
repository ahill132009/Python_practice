class SpaceObject:
	def __init__(self, name=None):
		self.name = name

class Planet(SpaceObject):
	def __init__(self, name, population=None):
		super().__init__(name)
		self.population = population or []

	def append_to_population(self, *new_animal):
		self.population.extend(new_animal)
		return f'{new_animal} having been appended'

	def __str__(self):
		if len(self.population) > 1:
			return f'{str(x) for population self.population} live on this planet'
		elif len(self.population) == 1:
			return f'{self.population} lives on this planet'
		else:
			return f'Nobody lives on this planet'

class Animal:
	def __init__(self, animal_name=None):
		self.animal_name = animal_name

	def __repr__(self):
		return f'{self.animal_name}'

class Cow(Animal):
	def __init__(self, animal_name):
		super().__init__(animal_name)

class Dog(Animal):
	def __init__(self, animal_name):
		super().__init__(animal_name)

class Cat(Animal):
	def __init__(self, animal_name):
		super().__init__(animal_name)

class Moose(Animal):
	def __init__(self, animal_name):
		super().__init__(animal_name)

