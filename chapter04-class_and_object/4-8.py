class Person:
	name = 'User'

class Student(Person):
	def __init__(self, school_name):
		self.school_name = school_name

if __name__ == '__main__':
	user = Student('小学')
	print(user.__dict__)   #显示属性字典
	print(Person.__dict__)
	print(dir(user))   #dir比__dict__显示增多属性名
	print(dir(Person))
