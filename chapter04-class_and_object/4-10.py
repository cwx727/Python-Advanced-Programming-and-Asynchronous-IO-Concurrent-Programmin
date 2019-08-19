class Human:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('Human',name, age)



class Student(Human):
	def __init__(self, school, name, age):    #name和age为父类的参数
		self.school = school
		super().__init__(name,age)    #继承父类的构造函数
		#super(Student, self).def_name(name,age)    #继承父类的函数
		print('Student',school,name,age)

if __name__ == '__main__':
	#human = Human('NAME', 'AGE')
	student = Student('SCHOOL', 'NAME', 'AGE')
	print(Student.__mro__)

