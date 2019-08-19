class Dog:
	def say(self):
		print('dog')

class Cat:
	def say(self):
		print('cat')

animals = [Dog,Cat]
for animal in animals:
	animal().say()

